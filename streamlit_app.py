import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Data Analyst Portfolio Dashboard", page_icon="📊", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Select a section to explore:")
section = st.sidebar.radio("Go to", ["Home", "Sales Analysis Demo", "Tech Stack"])

# Home Section
if section == "Home":
    st.title("🚀 Data Analyst Portfolio Demo")
    st.markdown("""
    Welcome to the interactive demo of my portfolio. This dashboard showcases my ability to:
    - **Analyze Data**: Using Python (Pandas) and SQL.
    - **Visualize Insights**: Creating interactive charts.
    - **Deploy Solutions**: Building user-friendly web apps.
    """)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Projects Completed", "5+", "Level 1-5")
    col2.metric("Tech Stack", "Python, SQL, Rust", "Full Stack")
    col3.metric("Business Impact", "High", "ROI Focused")

    try:
        image = Image.open('images/dashboard_preview.png')
        st.image(image, caption='Snapshot of Static Analysis', use_column_width=True)
    except Exception as e:
        st.warning("Preview image not found. Ensure 'images/dashboard_preview.png' exists.")

# Sales Analysis Demo
elif section == "Sales Analysis Demo":
    st.title("📊 Sales Trend Analysis")
    st.markdown("This is a **simulated live view** of a sales dataset, similar to the one used in Level 1 & 2 projects.")

    # Generate synthetic data for demo
    dates = pd.date_range(start="2023-01-01", periods=100)
    data = pd.DataFrame({
        "Date": dates,
        "Sales": np.random.randint(100, 500, size=100),
        "Region": np.random.choice(["North", "South", "East", "West"], size=100),
        "Category": np.random.choice(["Electronics", "Clothing", "Home", "Toys"], size=100)
    })

    # Metrics
    total_sales = data["Sales"].sum()
    avg_sales = data["Sales"].mean()
    
    m1, m2 = st.columns(2)
    m1.metric("Total Sales (Simulated)", f"${total_sales:,.0f}")
    m2.metric("Average Daily Sales", f"${avg_sales:.2f}")

    # Charts
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Sales Over Time")
        st.line_chart(data.set_index("Date")["Sales"])

    with c2:
        st.subheader("Sales by Region")
        fig, ax = plt.subplots()
        sns.barplot(data=data, x="Region", y="Sales", estimator=sum, ax=ax, palette="viridis")
        st.pyplot(fig)

    st.subheader("Raw Data Preview")
    st.dataframe(data.head())

# Tech Stack Section
elif section == "Tech Stack":
    st.title("🛠️ Technical Capabilities")
    
    st.markdown("### Core Competencies")
    st.code("""
    - Languages: Python, SQL, Rust
    - Libraries: Pandas, Polars, NumPy, Scikit-Learn
    - Visualization: Matplotlib, Seaborn, Streamlit, Tableau
    - Databases: PostgreSQL, SQLite
    """, language="text")

    st.info("Check out the full code in the GitHub repository!")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit by Andree Salazar")
