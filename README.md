🌍 Gen-AI Climate Risk & Insurance Insight Agent

🧠 Project Overview

This project is built for the Chubb Hackathon Challenge and aims to empower Gen-AI to enhance climate risk awareness and streamline insurance insights. It leverages state-of-the-art AI models to:

Scrape news and reports from legitimate sources.

Analyze climate and insurance-related information.

Summarize and categorize the insights.

Visualize climate risk trends in Hyderabad.

Developed exclusively by female talent to promote underrepresented innovation in tech.

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

git clone https://github.com/yourusername/climate-risk-agent
cd climate-risk-agent

2. Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Run the Streamlit App

streamlit run app/main_app.py

📈 Output Format (Sample)

{
  "title": "Hyderabad sees record temperatures in July",
  "summary": "New climate records broken in Hyderabad...",
  "tags": ["Climate Risk", "Policies"],
  "forecast_consistency": {
    "match": true,
    "reason": "Heatwave detected in 7/2023 (5 days)"
  },
  "validation": {
    "confidence": 80,
    "flags": ["May lack insurance relevance"]
  },
  "references": [
    "https://scholar.google.com/scholar?q=Hyderabad+heatwave",
    "https://scholar.google.com/scholar?q=climate+change+insurance"
  ]
}

📊 Evaluation Metrics

Metric

Description

✅ Source Relevance

Are news scraped from authentic domains?

🏷️ Classification Accuracy

Is article labeled in the correct risk category?

🔁 Consistency Score

Does news content match Hyderabad weather records?

📄 Summary Clarity

Is the insight concise and coherent?

✅ Ethical Considerations

All AI decisions are explainable.

No personal/private data is used or scraped.

News is sourced from public, credible feeds.

Designed to assist—not replace—human underwriters.

👩‍💻 Contributors

Built by: [Your Name]For: Chubb Female Hackathon Challenge

Feel free to reach out or fork this repo to improve the insights further!