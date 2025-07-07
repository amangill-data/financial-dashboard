import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("financial_ratios_winsorized.csv")  # Make sure this file is in Downloads

st.title("Financial Ratios Interactive Dashboard")

# Industry Selection
industry = st.selectbox("Choose Industry", df["gicdesc"].dropna().unique())

# Filtered Data Frame 
filtered_df = df[df["gicdesc"] == industry]

# 1. Histogram for Current Ratio
st.subheader("Distribution of Current Ratio")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df["curr_ratio_Median"], kde=True, ax=ax1)
st.pyplot(fig1)

# 2. Boxplot for Quick Ratio
st.subheader("Boxplot of Quick Ratio")
fig2, ax2 = plt.subplots()
sns.boxplot(x=filtered_df["quick_ratio_Median"], ax=ax2)
st.pyplot(fig2)

# 3. Correlation Heatmap
st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)
