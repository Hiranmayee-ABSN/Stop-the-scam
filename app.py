import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="🕵️ Job Fraud Detector", layout="wide")
st.title("🕵️‍♂️ Job Fraud Detection Dashboard")
st.write("Upload a job listings CSV file to detect potentially fraudulent postings.")

model = joblib.load("fraud_model.pkl")

uploaded_file = st.file_uploader("📁 Upload Job Listings CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded and loaded successfully!")

        df.fillna("", inplace=True)

        text_column = "description"
        if text_column not in df.columns:
            st.error(f"❌ Column '{text_column}' not found in uploaded CSV.")
        else:
            X = df[text_column].astype(str)

            predictions = model.predict(X)
            probabilities = model.predict_proba(X)[:, 1]

            df_results = df.copy()
            df_results['fraudulent'] = predictions
            df_results['fraud_probability'] = probabilities

            fraud_count = df_results['fraudulent'].sum()
            total_jobs = len(df_results)
            fraud_percent = round((fraud_count / total_jobs) * 100, 2)

            st.markdown(
                f"""
                <div style="background-color:#FFE0E0;padding:20px;border-radius:12px;text-align:center;">
                    <h2 style="color:#E53935;">🚨 Alert: {fraud_percent}% of job listings are likely fraudulent!</h2>
                </div>
                """, unsafe_allow_html=True
            )

            st.subheader("📊 Visual Insights")
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 🔍 Fraud Probability Distribution")
                fig1, ax1 = plt.subplots(figsize=(5, 3))
                sns.histplot(df_results['fraud_probability'], bins=20, color="skyblue", kde=True, ax=ax1)
                ax1.set_xlabel("Fraud Probability")
                ax1.set_ylabel("Frequency")
                st.pyplot(fig1)

            with col2:
                st.markdown("#### 📌 Fraud vs Genuine Overview")
                fig2, ax2 = plt.subplots(figsize=(5, 3))
                values = df_results['fraudulent'].value_counts().sort_index()
                fraud_labels = ['Genuine' if i == 0 else 'Fraudulent' for i in values.index]
                ax2.pie(values, labels=fraud_labels, autopct='%1.1f%%', startangle=140,
                        colors=["#66bb6a", "#ef5350"][:len(values)])
                ax2.axis("equal")
                st.pyplot(fig2)

            st.subheader("🔎 Top 10 Most Suspicious Job Listings")
            top_frauds = df_results.sort_values("fraud_probability", ascending=False).head(10)
            st.dataframe(top_frauds[[text_column, 'fraud_probability']])

            st.subheader("📥 Download Prediction Results")
            csv_data = df_results.to_csv(index=False).encode("utf-8")
            st.download_button("Download Results as CSV", csv_data, "fraud_predictions.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("👆 Upload a CSV file to get started.")
