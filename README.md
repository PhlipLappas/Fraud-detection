Custom Fraud Detection System (Built from Scratch) 🛡️
A pure Python implementation of a Logistic Regression engine designed to identify fraudulent transactions. This project demonstrates the core mechanics of machine learning optimization without the use of high-level libraries like Scikit-Learn or TensorFlow.

💡 Overview
This system processes transaction data and learns to distinguish between legitimate and fraudulent activities through an iterative training process. Instead of using "black-box" tools, I manually implemented the training logic to understand exactly how weights affect the outcome.

Key Logic:
Data Handling: Parses historical transaction data directly from CSV files.

Probability Mapping: Implements the Sigmoid function to squash raw calculations into a probability range (0% to 100%).

Training (Gradient Descent): The model calculates its own error and adjusts its internal weights to improve accuracy over time.

Mathematical Stability: Includes custom safeguards to prevent "logarithmic overflow," ensuring the program doesn't crash when probabilities are near absolute 0 or 1.

✨ Features
Zero Dependencies: Written in standard Python 3 (using only the math and csv modules).

Interactive CLI: A built-in command-line interface allows users to input transaction details manually and get real-time fraud probability.

Explainable AI: Unlike complex neural networks, this model's decisions are transparent and based on weight values that can be inspected and analyzed.

🚀 Getting Started
Clone the repository:

Bash
git clone https://github.com/PhilipLappas/Fraud-Detection-System.git
Run the application:

Bash
python main.py
Test a transaction:
Input the requested details (amount, time, etc.) when prompted to see if the system flags the transaction as fraud.

🛠 Roadmap
[ ] Vectorization: Re-writing the core engine to use Linear Algebra (NumPy) for handling hundreds of features simultaneously.

[ ] Data Visualization: Integrating simple plots to show the error reduction during training.

[ ] Web Interface: Creating a simple GUI/Web-app for easier interaction.

Developed by me Aspiring Machine Learning Engineer | Focus on Algorithmic Foundations

