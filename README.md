🌍 Gen-AI Climate Risk & Insurance Insight Agent

🧠 Project Overview

This project is built to empower Gen-AI to enhance climate risk awareness and streamline insurance insights. It leverages state-of-the-art AI models to:
Scrape news and reports from legitimate sources.
Analyze climate and insurance-related information.
Summarize and categorize the insights.
Visualize climate risk trends in Hyderabad.

🚀 Features
🔍 Live News Fetching: From sources like Reuters, Guardian, TNFD.
🧠 LLM Summarization: Extract structured insights from long articles.
🏷️ Auto-Tagging: Classifies news into categories (Climate Risk, InsureTech, etc.).
✅ Validation Module: Ensures insurance relevance and Hyderabad context.
📊 Forecast Analyzer: Cross-checks news with historical weather patterns.
📈 Interactive Visualizations: Heatwave trends and rainfall anomalies for Hyderabad.

🏗️ Architecture
Workflow Diagram:

User selects mode (recent/historical/rss)
            |
        [Streamlit UI]
            |
        run_pipeline()
            |
     +-------------------+
     | News Fetch Module |
     +-------------------+
              |
     +----------------------+
     | Summarizer (LLM)     |
     +----------------------+
              |
     +---------------------+
     | Article Classifier   |
     +---------------------+
              |
     +---------------------+
     | Weather Consistency  |
     | Validator & Forecast |
     +---------------------+
              |
     +---------------------+
     | Reference Generator  |
     +---------------------+
              |
         Final Report

System Components:
main.py: Core agent logic.
fetch_news.py: Pulls articles via RSS and Tavily.
summarizer.py: Summarizes using HuggingFace BART.
classifier.py: Zero-shot classification with BART-MNLI.
analyze_forecast.py: Weather anomaly checks.
visualizer.py: Streamlit charting.


📂 Sources Used
The Guardian - Climate Crisis RSS
Reuters - Environment News
Insurance Journal - Catastrophe
TNFD Reports
Hyderabad Weather Dataset


⚙️ Setup Guide
1. Clone the Repository
git clone https://github.com/naaz-verma/weather-report-LLM
cd weather-report-LLM

2. Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Run the Streamlit App
streamlit run app/main_app.py

📈 Output Format 

🔹 **Title**: Telangana Sees 3-Fold Increase in Heat Stroke Cases in April
🔹 **Summary**: The heatwave in Telangana in 2024, meanwhile, has been exceptionally severe, with temperatures reaching unprecedented highs. “The state recorded
🔹 **Tags**: Climate Risk, Impact on Underwriting
🔹 **Forecast Consistency**: {'match': False, 'reason': 'No data available for unknown month/1104'}
🔹 **References:**
    - https://scholar.google.com/scholar?q=Hyderabad
    - https://scholar.google.com/scholar?q=severe temperatures
    - https://scholar.google.com/scholar?q=weather trends
    - https://scholar.google.com/scholar?q=highs state
    - https://scholar.google.com/scholar?q=heatwave
    - https://scholar.google.com/scholar?q=2024 exceptionally
    - https://scholar.google.com/scholar?q=climate change
    - https://scholar.google.com/scholar?q=insurance
    - https://scholar.google.com/scholar?q=heatwave telangana
    - https://scholar.google.com/scholar?q=recorded
🔹 **Content Validation**: {'confidence': 60, 'flags': ['May lack insurance relevance', 'Missing location context: Hyderabad']}

📊 Evaluation Metrics
Metric
Description
✅ Source Relevance - Are news scraped from authentic domains?
🏷️ Classification Accuracy - Is article labeled in the correct risk category?
🔁 Consistency Score - Does news content match Hyderabad weather records?
📄 Summary Clarity - Is the insight concise and coherent?
✅ Ethical Considerations - All AI decisions are explainable.
No personal/private data is used or scraped.
News is sourced from public, credible feeds.
Designed to assist—not replace—human underwriters.

👩‍💻 Contributors

Built by: Naaz Verma

Feel free to reach out or fork this repo to improve the insights further!
