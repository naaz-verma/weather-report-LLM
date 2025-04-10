
# Imports
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
import getpass
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults

# openai_apikey = 
# tavily_key = 

# # agent/fetch_news.py
# from langchain_community.tools.tavily_search import TavilySearchResults

# def fetch_climate_news(query: str = "climate change insurance risks"):
#     tool = TavilySearchResults(
#         max_results=5,
#         search_depth="advanced",
#         include_answer=True,
#         include_raw_content=True,
#         api_key=os.getenv("TAVILY_API_KEY")
#     )
#     return tool.invoke({"query": query})


# # You could always choose to differ
# model = ChatOpenAI(model="gpt-3.5-turbo-1106", api_key = openai_apikey)

# # Sample tool definition to get you started, you can explore further and more~
# tool = TavilySearchResults(
#     max_results=100,
#     search_depth="advanced",
#     include_answer=True,
#     include_raw_content=True,
#     include_images=True,
#     # include_domains=[...],
#     # exclude_domains=[...],
#     # name="...",            # overwrite default tool name
#     # description="...",     # overwrite default tool description
#     # args_schema=...,       # overwrite default args_schema: BaseModel
# )

# response = tool.invoke({"query": "your prompt"})

# def structure_the_response(response, *args):
#     """
    
#     Your code goes here.
#     This function is set as a placeholder to get guide to the results expectations. You can always have own approach to set the functions.
    
#     """

#     return structured_response


# def find_research_references_correlating_with_each_news_snnipets(structured_response):
#     """
#     Your code goes here.
#     This function is set as a placeholder to get guide to the results expectations. You can always have own approach to set the functions.
    

#     Expection with this block is to have a comparison of the news with the ground truth so that the legitimacy of the report could be
#     maintanined.
#     """

#     return enriched_responses, references_dict


# def define_ui_and_visual_elements(enriched_responses, references_dict):
#     """
#     Your code goes here.
#     This function is set as a placeholder to get guide to the results expectations. You can always have own approach to set the functions.
    
#     """

#     return updated_risks_report


# ### App UI Section ###


# import streamlit as st

# ## Sample data which you source from "enriched_responses" & "references_dict" as prepared above:

# news_articles = [
#     {
#         "title": "Insurance risks will be a proxy carbon tax",
#         "source": "Reuters",
#         "date": "2024-12-27",
#         "summary": "In 2025, the insurance sector is expected to reflect climate impacts via higher premiums, effectively acting as a proxy carbon tax.",
#         "tags": ["parametric insurance", "basis risk", "climate change"]
#     },
#     {
#         "title": "Monday briefing: What if the climate crisis makes disaster insurance unaffordable?",
#         "source": "The Guardian",
#         "date": "2025-01-27",
#         "summary": "Wildfires and floods are challenging the viability of disaster insurance, with major markets in the US and UK adjusting to increased risks.",
#         "tags": ["disaster insurance", "home insurance", "climate risk"]
#     },
# ]

# research_papers = [
#     {
#         "title": "Managing Basis Risks in Weather Parametric Insurance",
#         "authors": "Hang Gao, Shuohua Yang, Xinli Liu",
#         "date": "2024-09-25",
#         "abstract": "This paper uses Monte Carlo simulations to demonstrate that portfolio diversification can significantly reduce basis risk in weather parametric insurance.",
#         "tags": ["basis risk", "parametric insurance", "Monte Carlo"]
#     },
#     {
#         "title": "Data-driven Parametric Insurance Framework Using Bayesian Neural Networks",
#         "authors": "Subeen Pang, Chanyeol Choi",
#         "date": "2022-09-22",
#         "abstract": "This work employs a deep sigma point process—a Bayesian neural network approach—to improve risk predictions for parametric insurance, providing uncertainty estimates alongside improved accuracy.",
#         "tags": ["Bayesian neural networks", "parametric insurance", "risk modeling"]
#     },
# ]


# ### Functional Design
# def filter_by_tag(data, selected_tag):
#     """Filter a list of items by checking if the selected tag is in their tags list."""
#     return [item for item in data if selected_tag in item["tags"]]

# def get_all_tags(datasets):
#     """Extract a sorted list of unique tags from multiple datasets."""
#     tags = set()
#     for data in datasets:
#         for item in data:
#             tags.update(item["tags"])
#     return sorted(tags)


# ### Layout design 
# st.title("Climate Risk Insurance Dashboard")

# # Sidebar for tag selection
# st.sidebar.header("Filter by Tag")
# all_tags = get_all_tags([news_articles, research_papers])
# selected_tag = st.sidebar.selectbox("Select a tag", all_tags)

# # Display filtered News Articles
# st.header(f"News Articles Tagged: {selected_tag}")
# filtered_news = filter_by_tag(news_articles, selected_tag)
# if filtered_news:
#     for article in filtered_news:
#         st.subheader(article["title"])
#         st.caption(f"{article['source']} | {article['date']}")
#         st.write(article["summary"])
#         st.markdown("---")
# else:
#     st.write("No news articles match this tag.")

# ### Interactions output Design
# st.header(f"Research Papers Tagged: {selected_tag}")
# filtered_research = filter_by_tag(research_papers, selected_tag)
# if filtered_research:
#     for paper in filtered_research:
#         st.subheader(paper["title"])
#         st.caption(f"{paper['authors']} | {paper['date']}")
#         st.write(paper["abstract"])
#         st.markdown("---")
# else:
#     st.write("No research papers match this tag.")

# st.sidebar.markdown("### About")
# st.sidebar.info(
#     "This dashboard integrates news and academic research on climate risk insurance. "
#     "Select a tag to see related items from both news and arXiv research."
# )
