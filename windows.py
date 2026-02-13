import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Multi-Platform Streamlit Dashboard",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stPlotlyChart {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Helper function to generate data
@st.cache_data
def get_data(days=30):
    dates = [datetime.now() - timedelta(days=x) for x in range(days)]
    dates.reverse()
    data = pd.DataFrame({
        'Date': dates,
        'Active Users': np.random.randint(100, 1000, size=days).cumsum(),
        'Revenue': np.random.uniform(1000, 5000, size=days).cumsum(),
        'Platform': np.random.choice(['Android', 'Windows', 'Web'], size=days)
    })
    return data

def main():
    st.sidebar.title("🚀 Navigation")
    page = st.sidebar.radio("Go to", ["Overview", "Data Analytics", "System Status", "DevOps Info"])

    st.sidebar.markdown("---")
    st.sidebar.info(f"Running: **windows.py**\n\nEnvironment: **{st.experimental_get_query_params().get('env', ['Production'])[0]}**")

    if page == "Overview":
        show_overview()
    elif page == "Data Analytics":
        show_analytics()
    elif page == "System Status":
        show_status()
    elif page == "DevOps Info":
        show_devops()

def show_overview():
    st.title("🖥️ Multi-Platform Overview")
    st.markdown("Welcome to your advanced Streamlit dashboard, optimized for **Android**, **Windows 11**, and **Streamlit Cloud**.")

    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Users", "12,450", "+5.2%")
    with col2:
        st.metric("Revenue", "$45,200", "+12.1%")
    with col3:
        st.metric("Uptime", "99.99%", "Stable")
    with col4:
        st.metric("Active Sessions", "432", "-2.4%")

    st.markdown("### Growth Trend")
    data = get_data()
    fig = px.area(data, x='Date', y='Revenue', title="Cumulative Revenue Over Time", color_discrete_sequence=['#00CC96'])
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, use_container_width=True)

def show_analytics():
    st.title("📊 Data Analytics")

    days = st.slider("Select timeframe (days)", 7, 90, 30)
    data = get_data(days)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Platform Distribution")
        fig_pie = px.pie(data, names='Platform', values='Active Users', hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("User Engagement")
        fig_scatter = px.scatter(data, x='Date', y='Active Users', color='Platform', size='Active Users', hover_name='Platform')
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Raw Dataset")
    st.dataframe(data, use_container_width=True)

def show_status():
    st.title("🚦 System Status")

    status_col1, status_col2 = st.columns(2)

    with status_col1:
        st.success("✅ Docker Container: Healthy")
        st.success("✅ Database Connection: Active")
        st.warning("⚠️ Cache Usage: 85%")

    with status_col2:
        st.info(f"Current Server Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.info("Deployment: Windows 11 via Docker Desktop")

    st.markdown("### Resource Usage")
    usage_data = pd.DataFrame({
        'Metric': ['CPU', 'RAM', 'GPU', 'Disk'],
        'Usage (%)': [34, 56, 12, 44]
    })
    st.bar_chart(usage_data.set_index('Metric'))

def show_devops():
    st.title("🛠️ DevOps Configuration")
    st.markdown("This project is built for high portability across different environments.")

    st.code("""
# Project Entry Point: windows.py
# Running on: Streamlit Cloud | Docker | Codespaces
    """, language="python")

    st.subheader("Quick Commands")
    st.info("**Windows 11 PowerShell:**\n`docker build -t my-app .` \n`docker run -p 8501:8501 my-app`")
    st.info("**Streamlit Cloud:**\nSet 'Main file path' to `windows.py` in advanced settings.")

if __name__ == "__main__":
    main()
