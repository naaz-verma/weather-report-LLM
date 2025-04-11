import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

def fetch_climate_news(query: str = "hyderabad heatwave impact on insurance in india", max_articles=3):
    tavily = TavilySearchResults(
        max_results=max_articles,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
        api_key=os.getenv("TAVILY_API_KEY")
    )
    return tavily.invoke({"query": query})