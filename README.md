# Stop-the-scam
# Job Fraud Detection
An interactive Streamlit web application that detects potentially **fraudulent job postings** using a trained Machine Learning model. Upload a job listings CSV and instantly get fraud predictions, visual insights, and downloadable results.

## Problem Statement

Fraudulent job listings waste time, harm trust, and pose real risks to job seekers. With thousands of listings generated daily, manual moderation is not scalable. This project aims to solve that by:
- Automatically identifying suspicious job listings using ML.
- Providing clear, visual fraud indicators in a simple dashboard.
- Allowing stakeholders to investigate high-risk jobs quickly.

## Features

- **Upload CSV**: Upload a job listing dataset (with relevant features).
- **ML-powered Detection**: Predicts if a job is *genuine* or *fraudulent* using a trained logistic regression model.
- **Interactive Visualizations**:
- Fraud Probability Histogram
- Pie Chart of Fraud vs Genuine Jobs
- **Top 10 Most Suspicious Jobs**: Lists high-risk jobs by fraud probability.
- **Download Results**: Download a CSV with predictions and fraud probabilities.
- **Live Fraud Rate Alert**: Shows percentage of listings predicted as fraudulent.
- 
## Tech Stack

| Layer         | Tools Used                           |
|---------------|--------------------------------------|
| Frontend    | Streamlit                           |
| Visualization | Matplotlib, Seaborn                 |
| Model       | Scikit-learn (Logistic Regression)   |
| Packaging   | joblib, pandas                       |


## Project Structure

job-fraud-detector/
│
├── app.py                 # Streamlit App
├── fraud\_model.pkl        # Trained ML Model
├── style.css              # Optional custom styling
├── test\_jobs.csv          # Sample job listings CSV
└── README.md              # You're here!


## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Hiranmayee-ABSN/job-fraud-detector.git
cd job-fraud-detector
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

## 📽️ Video Presentation

Watch our full walkthrough demo:
📺 **[Video Link – YouTube / Google Drive](https://your-link.com)**


## 🙋 About the Developer

👤 **Solo Developer**
Built in 36 hours during a hackathon with the assistance of ChatGPT for rapid prototyping and debugging.

## 📌 Acknowledgments

* Dataset inspired by [Kaggle Job Fraud Detection Dataset](https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction)
* Streamlit for quick and beautiful dashboards
* Scikit-learn for fast ML modeling
* 
## 📃 License
This project is for academic and demonstration purposes only.
