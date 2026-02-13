import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Attempt to import plotly with error handling
try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

st.set_page_config(page_title="Docker Streamlit App", page_icon="🐳")

st.title('Hello from Docker! 🐳')
st.write('This Streamlit app is running inside a Docker container.')

st.header('Sample Data')
try:
    df = pd.DataFrame({
        'Column A': np.random.randn(10),
        'Column B': np.random.randn(10)
    })

    if PLOTLY_AVAILABLE:
        st.subheader("Interactive Plotly Chart")
        fig = px.line(df, title="Random Walk")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.subheader("Native Streamlit Chart")
        st.line_chart(df)

except Exception as e:
    st.error(f"Error generating chart: {e}")

st.header('User Input')
name = st.text_input('Enter your name', 'World')
st.write(f'Hello, {name}!')

st.sidebar.info(f"Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
