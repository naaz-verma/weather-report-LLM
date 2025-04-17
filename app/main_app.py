# app/main_app.py
import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from visualizer import plot_heatwave_timeline
    
from backend.main import main as run_pipeline

st.set_page_config(page_title="Climate Risk Analyzer", layout="wide")
st.title("🌦️ Weather & Climate Report Analyzer")
st.markdown("""
        Welcome! This app analyzes and visualizes climate-related news and data using different modes:

        - **Analyzer View**: 📊 View news analysis on climate risk and impact on insurance.
        - **Charts View**: 📊 View visualizations for historical and recent data in Hyderabad.

        Choose a section from the sidebar to get started!
        """)


# Sidebar
with st.sidebar:
    st.header("⚙️ Navigation")
    section = st.selectbox("Go to Section", ["Analyzer", "Charts"])

if section == "Analyzer":
    st.markdown("""
        Welcome! This app analyzes climate-related news and data using different modes:

        - **RSS Mode**: 📡 Fetches **latest climate news from around the world**.
        - **Historical Mode**: 🕰️ Focuses on **past weather events in Hyderabad**, comparing with actual temperature datasets.
        - **Recent Mode**: 🔎 Uses **recent Hyderabad weather data** and compares it to forecasts and related news to identify alignment or discrepancies.
    

        Choose mode and output format from the sidebar to get started!
        """)
    with st.sidebar:
        mode = st.selectbox("Select News Mode", ["recent", "historical", "rss"])
        output_style = st.radio("Output Style", ["bullet", "json"])

    if st.button("Run Analyzer"):
        with st.spinner("Processing news..."):
            articles = run_pipeline(mode=mode, output_style=output_style)

        if articles:
            st.success(f"✅ {len(articles)} articles processed.")
            for article in articles:
                st.subheader(article['title'])
                st.markdown(f"**Summary:** {article['summary']}")
                st.markdown(f"**Tags:** `{', '.join(article.get('tags', []))}`")
                st.markdown(f"**Forecast Match:** {article['forecast_consistency']}")
                st.markdown(f"**Validation:** {article['validation']}")
                st.markdown(f"[Read More]({article['url']})")

                with st.expander("📚 References"):
                    for ref in article['references']:
                        st.markdown(f"- [{ref}]({ref})")

        
        else:
            st.warning("⚠️ No articles returned.")

elif section == "Charts":
    st.header("📊 Hyderabad Climate Risk Charts")
    st.markdown("""
This section provides visual insights based on **Hyderabad's recent and historical climate data**.
You'll find chart for:
- **Heatwave timelines**
    """)
    if st.button("Show Charts"):
        with st.spinner("Generating visualizations..."):
            plot_heatwave_timeline()
