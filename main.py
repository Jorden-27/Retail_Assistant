import streamlit as st
from agent import create_sql_agent

st.set_page_config(page_title="🛍️ Retail Q&A Bot", layout="centered")
st.title("🛒 Gemini-Powered Retail Q&A Bot")

query = st.text_input("Ask me anything about your products or discounts:")

if query:
    with st.spinner("Thinking..."):
        try:
            agent = create_sql_agent()
            response = agent.run(query)
            st.success(response)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
