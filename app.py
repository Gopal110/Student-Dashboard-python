import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Student Dashboard", layout="wide")

# Title
st.title("🎓 Student Marks Analysis Dashboard")

# Load data
df = pd.read_csv("StudentsPerformance.csv")

# Sidebar filter
st.sidebar.header("🔍 Filter Students")
student = st.sidebar.multiselect(
    "Select Students",
    options=df["Name"].unique(),
    default=df["Name"].unique()
)

filtered_df = df[df["Name"].isin(student)]

# KPIs
avg_total = filtered_df[["Maths", "Science", "English", "Computer"]].mean().mean()
topper = (
    filtered_df.set_index("Name")[["Maths", "Science", "English", "Computer"]]
    .sum(axis=1)
    .idxmax()
)

col1, col2 = st.columns(2)
col1.metric("📊 Overall Average Marks", f"{avg_total:.1f}")
col2.metric("🏆 Top Performer", topper)

# Average marks per subject
st.subheader("📊 Average Marks per Subject")
avg_marks = filtered_df[["Maths", "Science", "English", "Computer"]].mean()

fig1, ax1 = plt.subplots()
sns.barplot(x=avg_marks.index, y=avg_marks.values, ax=ax1)
ax1.set_xlabel("Subject")
ax1.set_ylabel("Average Marks")
st.pyplot(fig1)

# Box plot
st.subheader("📦 Subject-wise Marks Distribution")
fig2, ax2 = plt.subplots()
sns.boxplot(data=filtered_df[["Maths", "Science", "English", "Computer"]], ax=ax2)
ax2.set_ylabel("Marks")
st.pyplot(fig2)

# Correlation heatmap
st.subheader("🔥 Subject Correlation Heatmap")
corr = filtered_df[["Maths", "Science", "English", "Computer"]].corr()

fig3, ax3 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

# Data table
st.subheader("📄 Student Marks Data")
st.dataframe(filtered_df)
