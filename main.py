import streamlit as st
from agent import create_sql_agent

st.set_page_config(
    page_title="👕 Retail Q&A Assistant",
    layout="centered"
)

# ---------------- Header ----------------
st.markdown(
    """
    <h1 style='text-align: center; color: #1E1E1E;'>🛍️ Clothing Brand Q&A Assistant</h1>
    <p style='text-align: center; font-size: 18px; color: #4F4F4F;'>
        Ask anything about our <b>t-shirts</b> — sizes, colors, brands, or discounts. Powered by Generative AI!
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- Sample Prompts ----------------
with st.expander("💡 Examples you can try"):
    st.markdown("""
    - *"What Nike t-shirts are available in black?"*
    - *"List all Levi's t-shirts in size M"*
    - *"What discounts are available on Van Heusen shirts?"*
    - *"Do you have Adidas shirts in red?"*
    """)

# ---------------- User Query Input ----------------
query = st.text_input("🔎 Ask your question about t-shirts below:")

# ---------------- Response Output ----------------
if query:
    with st.spinner("🤖 Thinking..."):
        try:
            agent = create_sql_agent()
            response = agent.run(query)
            st.success(response)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
