# app/ui_components.py
import streamlit as st

def article_card(article):
    st.markdown(f"### {article['title']}")
    st.markdown(f"**Summary:** {article['summary']}")
    st.markdown(f"**Tags:** `{', '.join(article.get('tags', []))}`")
