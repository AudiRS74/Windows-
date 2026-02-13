import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Streamlit DevOps Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🚀 Streamlit DevOps Interactive Dashboard")
    st.markdown("---")

    # Sidebar for interactive controls
    st.sidebar.header("Dashboard Controls")

    app_mode = st.sidebar.selectbox(
        "Choose the App Mode",
        ["Home", "Data Explorer", "Visualization", "About"]
    )

    if app_mode == "Home":
        show_home()
    elif app_mode == "Data Explorer":
        show_data_explorer()
    elif app_mode == "Visualization":
        show_visualization()
    elif app_mode == "About":
        show_about()

def show_home():
    st.header("Welcome to your Dockerized Streamlit App!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Status", value="Running", delta="Healthy")
    with col2:
        st.metric(label="Environment", value="Docker", delta="Windows 11 Ready")
    with col3:
        st.metric(label="Last Updated", value=datetime.now().strftime("%H:%M:%S"))

    st.info("This application is running inside a Docker container. It's designed to be portable and consistent across different environments.")

    st.subheader("Quick Start Features")
    st.write("- **Data Explorer**: Generate and filter synthetic data.")
    st.write("- **Visualization**: Interactive charts using Plotly.")
    st.write("- **DevOps Ready**: Built-in Docker and GitHub Actions support.")

def show_data_explorer():
    st.header("📊 Data Explorer")

    # User input for data generation
    num_rows = st.slider("Select number of rows", min_value=10, max_value=1000, value=100)

    # Generate synthetic data with error handling
    try:
        data = pd.DataFrame({
            'Timestamp': pd.date_range(start='2024-01-01', periods=num_rows, freq='H'),
            'Value_A': np.random.randn(num_rows).cumsum(),
            'Value_B': np.random.randn(num_rows).cumsum(),
            'Category': np.random.choice(['Alpha', 'Beta', 'Gamma', 'Delta'], num_rows)
        })

        st.write("### Raw Data Preview")
        st.dataframe(data.head(10), use_container_width=True)

        st.write("### Data Statistics")
        st.write(data.describe())

        # Download button
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='synthetic_data.csv',
            mime='text/csv',
        )

    except Exception as e:
        st.error(f"An error occurred while generating data: {e}")

def show_visualization():
    st.header("📈 Interactive Visualizations")

    # Generate some data
    df = pd.DataFrame({
        'x': np.random.randn(500),
        'y': np.random.randn(500),
        'color': np.random.choice(['Type 1', 'Type 2', 'Type 3'], 500)
    })

    viz_type = st.radio("Select Visualization Type", ["Scatter Plot", "Histogram", "Line Chart"])

    if viz_type == "Scatter Plot":
        fig = px.scatter(df, x='x', y='y', color='color', title="Interactive Scatter Plot")
        st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Histogram":
        fig = px.histogram(df, x='x', color='color', barmode='overlay', title="Interactive Histogram")
        st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Line Chart":
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['A', 'B', 'C']
        )
        st.line_chart(chart_data)

def show_about():
    st.header("ℹ️ About this Project")
    st.write("""
    This project demonstrates a professional-grade DevOps setup for a Streamlit application.

    **Key Components:**
    - **Streamlit**: For the interactive web interface.
    - **Docker**: For containerization and easy deployment.
    - **GitHub Actions**: For automated building and testing.
    - **GitHub Codespaces**: For a cloud-based development environment.
    """)

    st.success("Everything is configured for a seamless 'Mobile -> Cloud -> Desktop' workflow.")

if __name__ == "__main__":
    main()
