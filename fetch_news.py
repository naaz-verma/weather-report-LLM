import os
import random
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

# Pool of query variations
query_templates = [
    "Hyderabad heatwave and climate impact on insurance",
    "Extreme heat events in Hyderabad between {start} and {end}",
    "Historical weather patterns in Hyderabad and insurance effects",
    "Heatwave insurance risks Hyderabad India {start}-{end}",
    "Hyderabad climate trends and insurance challenges over decades",
    "Hyderabad weather analysis and policy shifts {start}-{end}",
]

def fetch_climate_news(mode="historical", max_articles=3):
    if mode == "recent":
        query = "Recent heatwaves in Hyderabad 2024 climate insurance"
    else:
        start_year = random.choice(range(1950, 2015, 10))
        end_year = start_year + 10
        query_template = random.choice(query_templates)
        query = query_template.format(start=start_year, end=end_year)
    
    tavily = TavilySearchResults(
        max_results=max_articles,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
        api_key=os.getenv("TAVILY_API_KEY")
    )
    return tavily.invoke({"query": query})

