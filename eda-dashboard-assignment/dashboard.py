import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from fetch_data import fetch_and_clean_data

# Fetch cleaned data
df = fetch_and_clean_data()

st.title("📊 Simple Data Dashboard")

# Step 1: Dataset preview
st.subheader("Dataset Preview")
st.write(df.head())

# Step 2: Posts per user analysisc
st.subheader("Posts per User")
posts_per_user = df.groupby("user_id").size()

fig1, ax1 = plt.subplots()
posts_per_user.plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# Step 3: Post length distribution
st.subheader("Post Length Distribution")
fig2, ax2 = plt.subplots()
df["post_length"].plot(kind="hist", bins=20, ax=ax2)
st.pyplot(fig2)