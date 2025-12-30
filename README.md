# 📰 Fake News Detection System (Python + Machine Learning)

A machine learning–based web application that classifies news articles as **True** or **Fake** using Natural Language Processing (NLP).  
The system is trained on real-world datasets and deployed using **Flask** for real-time prediction.

---

## 🚀 Project Overview

This project uses:
- **TF-IDF Vectorization** for text feature extraction  
- **Multinomial Naive Bayes** for classification  
- **Flask** to serve predictions through a web interface  

Users can paste a news article, and the system will instantly determine whether it is **True News** or **Fake News**.

---

## 🧠 Machine Learning Workflow

1. Load True and Fake news datasets  
2. Label data (True = 0, Fake = 1)  
3. Combine and split dataset  
4. Train NLP model using TF-IDF + Naive Bayes  
5. Deploy trained model via Flask  
6. Predict article authenticity in real time  

---

## 📂 Project Files

fake_news_project/

│── fake_new.py        # Main Flask application  

│── True.csv           # True news dataset  

│── Fake.csv           # Fake news dataset  

│── model.pkl          # Trained ML model (optional)  

│── index.html         # Frontend UI  

│── project_pdf.pdf    # Project documentation  

> Note: Files are uploaded individually (no folder structure required).

---

## Requirements


Python **3.8+**

Install dependencies:
bash
pip install flask pandas scikit-learn

---

### ▶️ How to Run the Project
## Step 1: Open Terminal / Command Prompt

Navigate to the directory where all files are stored:

cd path/to/fake_news_project

## Step 2: Run the Flask Application
python fake_new.py

## Step 3: Open in Browser

Open:

http://127.0.0.1:5000

## Step 4: Test the System

Paste a news article

Click Predict

Get instant result:

✅ True News

❌ Fake News

--- 

## 🧪 Model Details

Algorithm: Multinomial Naive Bayes

Text Processing: TF-IDF Vectorizer

Dataset Split: 80% Training / 20% Testing

Output: JSON response via Flask API

---

## 📌 Technologies Used

Python

Flask

Pandas

Scikit-learn

HTML

---


## 👨‍💻 Author

**Shayan Qureshi**  

Software & AI Enthusiast

BS Artificial Intelligence – Semester 4 

https://github.com/Shayan-Qureshi4

---

## 📄 License

This project is developed for **educational purposes** and academic learning.





