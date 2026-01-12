# Transaction Fraud Detection using Machine Learning

## 📌 Project Overview

This project implements a **Transaction Fraud Detection System** using **Machine Learning** to identify fraudulent financial transactions. The system is trained on a real-world inspired dataset and deployed as a **Flask web application** that predicts whether a transaction is **Fraudulent** or **Legitimate** based on transaction details.

This project is designed for **college submission**, **viva**, and **demonstration purposes**.

---

## 🎯 Objectives

* Detect fraudulent transactions using historical transaction data
* Apply supervised machine learning for binary classification
* Build a user-friendly web interface for real-time prediction
* Demonstrate end-to-end ML workflow (data → model → deployment)

---

## 🛠️ Technology Stack

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn
* **Web Framework:** Flask
* **Frontend:** HTML, CSS
* **Dataset Source:** Kaggle (PaySim – Financial Transaction Dataset)
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
Fraud_Detection_Kaggle_Project/
│
├── dataset/                  # Dataset folder (CSV excluded from GitHub)
│   └── transactions.csv
│
├── model/                    # Trained model (ignored in GitHub)
│   └── fraud_model.pkl
│
├── templates/                # Frontend templates
│   └── index.html
│
├── app.py                    # Flask application
├── train_model.py            # ML model training script
├── requirements.txt          # Project dependencies
├── .gitignore                # Ignored files configuration
└── README.md                 # Project documentation
```

---

## 📊 Dataset Information

* **Dataset Name:** PaySim – A Financial Mobile Money Simulator
* **Source:** Kaggle
* **Link:** [https://www.kaggle.com/datasets/ealaxi/paysim1](https://www.kaggle.com/datasets/ealaxi/paysim1)

### Important Features Used:

* `amount`
* `oldbalanceOrg`
* `newbalanceOrig`
* `oldbalanceDest`
* `newbalanceDest`
* `isFraud` (Target Variable)

⚠️ **Note:** The dataset file is large (>100MB), so it is **excluded from the GitHub repository** and must be downloaded manually from Kaggle.

---

## 🧠 Machine Learning Model

* **Algorithm Used:** Random Forest Classifier
* **Type:** Supervised Learning (Binary Classification)
* **Why Random Forest?**

  * High accuracy
  * Handles imbalance well
  * Easy to explain in viva

The model learns patterns from transaction amounts and balance changes to predict fraudulent activity.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Chiku06/fraud-detection-project-kegal.git
cd fraud-detection-project-kegal
```

### 2️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Download Dataset

* Download dataset from Kaggle link above
* Rename file to:

```
transactions.csv
```

* Place it inside:

```
dataset/transactions.csv
```

### 4️⃣ Train the Model

```bash
python train_model.py
```

### 5️⃣ Run Flask App

```bash
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🖥️ Web Application Features

* Simple and clean user interface
* Accepts transaction details as input
* Displays prediction result instantly
* Real-time fraud detection

---

## 🧪 Sample Prediction Output

* ✅ **Legitimate Transaction**
* 🚨 **Fraud Transaction**

---

## 🧾 Viva / Examination Explanation

> “This project uses machine learning to detect fraudulent financial transactions. A Random Forest classifier is trained on a real-world inspired dataset. The trained model is deployed using Flask, allowing users to check transactions in real time.”

---

## ⚠️ GitHub File Size Notice

Due to GitHub’s file size limit:

* Large datasets and trained model files are excluded
* Dataset is referenced via Kaggle

This follows **industry best practices**.

---

## 🔮 Future Enhancements

* Add more features for higher accuracy
* Deploy the application on cloud platforms
* Improve UI using Streamlit or React
* Add transaction history and analytics dashboard

---

## 👨‍🎓 Academic Declaration

This project is developed for **educational purposes** as part of a **college machine learning project**.

---

## ⭐ Acknowledgements

* Kaggle for dataset
* Scikit-learn & Flask documentation

---

## 📬 Contact

**Student Name:** Kuldeep Sharma
**Course:** BCA
**University:** Galgotias University

---

⭐ *If you found this project useful, feel free to star the repository!*
