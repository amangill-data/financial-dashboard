import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("financial_ratios_winsorized.csv")

# Ensure numeric types
df['roe_Median'] = pd.to_numeric(df['roe_Median'], errors='coerce')
df['CAPEI_Median'] = pd.to_numeric(df['CAPEI_Median'], errors='coerce')
df['de_ratio_Median'] = pd.to_numeric(df['de_ratio_Median'], errors='coerce')

# Streamlit layout
st.title("Financial Ratios Dashboard")
st.write("Explore key financial metrics across industries.")

# Interactive dropdown for sector filter if available
if 'gicdesc' in df.columns:
    sector = st.selectbox("Select Industry Sector:", options=['All'] + sorted(df['gicdesc'].dropna().unique().tolist()))
    if sector != 'All':
        df = df[df['gicdesc'] == sector]

# Histogram: ROE
st.subheader("Return on Equity (ROE) Distribution")
fig1, ax1 = plt.subplots(figsize=(8,5))
sns.histplot(df['roe_Median'], kde=True, bins=30, ax=ax1)
ax1.set_title("Histogram of ROE")
st.pyplot(fig1)

# Scatter plot: ROE vs CAPEI
st.subheader("ROE vs CAPEI Scatter Plot")
fig2, ax2 = plt.subplots(figsize=(8,5))
sns.scatterplot(x='roe_Median', y='CAPEI_Median', data=df, ax=ax2)
ax2.set_title("Scatter Plot: ROE vs CAPEI")
st.pyplot(fig2)

# Box plot: Debt-to-Equity Ratio
st.subheader("Debt-to-Equity Ratio Box Plot")
fig3, ax3 = plt.subplots(figsize=(6,5))
sns.boxplot(y=df['de_ratio_Median'], ax=ax3)
ax3.set_title("Box Plot: Debt-to-Equity Ratio")
st.pyplot(fig3)

st.write("Dashboard created to support insights on profitability, valuation, and leverage.")
