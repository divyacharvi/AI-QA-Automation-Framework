import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI QA Dashboard", layout="wide")

st.title("🧠 AI QA Automation Framework Dashboard")

# Load results
df = pd.read_csv("outputs/results.csv")

st.subheader("📊 Dataset Overview")
st.write(df.head())

# ----------------------------
# Safety Score Distribution
# ----------------------------
st.subheader("📈 Safety Score Distribution")

fig, ax = plt.subplots()
ax.hist(df["safety_score"], bins=10)
st.pyplot(fig)

# ----------------------------
# Toxicity Analysis
# ----------------------------
st.subheader("☣️ Toxicity Score Analysis")

df["toxicity_score"] = df["toxicity"].apply(lambda x: eval(x)[0]["score"])

fig2, ax2 = plt.subplots()
ax2.hist(df["toxicity_score"], bins=10)
st.pyplot(fig2)

# ----------------------------
# Injection Risk Count
# ----------------------------
st.subheader("⚠️ Injection Risk Distribution")

risk_counts = df["injection_risk"].value_counts()

fig3, ax3 = plt.subplots()
ax3.bar(risk_counts.index, risk_counts.values)
st.pyplot(fig3)

# ----------------------------
# Summary Metrics
# ----------------------------
st.subheader("📌 Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Samples", len(df))
col2.metric("Avg Safety Score", round(df["safety_score"].mean(), 2))
col3.metric("Avg Toxicity", round(df["toxicity_score"].mean(), 4))