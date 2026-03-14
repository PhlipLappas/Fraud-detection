import csv
import math
x = []
y = []

with open("fraud_transactions.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(
            (int(row['hour']),
            float(row['amount']),
            int(row['is_foreign']),
            int(row['tx_last_1h']))
        )
        y.append(1 if int(row["fraud"]) == 1 else 0)
def sigmoid(z):
    if z >= 0:
        return 1 / (1 + math.exp(-z))
    else:
        exp_z = math.exp(z)
        return exp_z / (1 + exp_z)
def manual_boundary(epochs = 50):
    lr,w1,w2,w3,w4,b = 0.001,0,0,0,0,0
    for epoch in range(epochs):
        total_loss = 0
        for i in range(len(x)):
            y_true = y[i]
            hour = x[i][0]
            amount = x[i][1]
            foreign = x[i][2]
            tx = x[i][3]
            z = hour*w1+amount*w2+foreign*w3+tx*w4+b
            p = sigmoid(z)
            p_safe = p_safe = max(1e-15, min(1 - 1e-15, p))
            loss = -(y_true * math.log(p_safe) + (1 - y_true) * math.log(1 - p_safe))
            total_loss+=loss
            error = p-y_true
            w1 = w1-lr*error*hour
            w2 = w2-lr*error*amount
            w3 = w3-lr*error*foreign
            w4 = w4-lr*error*tx
            b = b-lr*error
    return(lr,w1,w2,w3,w4,b)                     


def predict(hour,amount,foreign,tx,w1,w2,w3,w4,b):
    z = w1*hour+w2*amount+foreign*w3+tx*w4+b
    p = sigmoid(z)
    return 1 if p>0.5 else 0
def accuracy(x,y,w1,w2,w3,w4,b):
    correct = 0
    for i in range(len(x)):
        hour = x[i][0]
        amount = x[i][1]
        foreign = x[i][2]
        tx = x[i][3]
        y_pred = predict(hour,amount,foreign,tx,w1,w2,w3,w4,b)
        if y_pred == y[i]:
            correct += 1
    return 100 * correct / len(x)
lr,w1,w2,w3,w4,b = manual_boundary(epochs=50)
 
print("This is the fraud detection system provided by Lappas.corp!")
hour = int(input("What was the exact time that the transaction was made?:"))
amount = float(input("What was the amount that was transacted?:"))
foreign = str(input("Was the transcation forward to a foreign country(yes/no):"))
if foreign =='yes':
    foreign = 1
else:
    foreign = 0
tx = int(input("How many transactions does this account have in the last hour:"))
pred = predict(hour,amount,foreign,tx,w1,w2,w3,w4,b)
if pred == 1:
    print("This transaction is a fraud")
else:
    print("This transaction is legit")