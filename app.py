import streamlit as st
from Model.model import LLM
from utils.logger import logger
from utils.handler import handle_exception


st.set_page_config(page_title="Poetic/Humorous LLM", page_icon=":tada:", layout="wide")

st.title("Text Rewriter App")
st.markdown("Use this app to rewrite your text in various styles and tones using the power of generative AI.")
with st.form("Chat_form", clear_on_submit=True):
    user_input = st.text_input("Enter your text here:", placeholder="Type your text...")
    col1, col2 = st.columns(2)
    with col1:
        selected_template_name = st.selectbox(
            "Choose a prompt template:",
            ("Simple", "Conversational", "RolePlaying"),
            index=0,
            help="Select a different template to change how the AI is prompted."
        )
    with col2:
        style_type = st.selectbox(
            "Choose a style:",
            ("humorous", "poetic"),
            index=0,
            help="Select the tone for the rewritten text."
        )
    submitted = st.form_submit_button("Rewrite Text")

if submitted:
    llm=LLM()
    output=llm.rewrite_text(user_input, style_type, selected_template_name.lower())
    reasoning,response=output.content.split("</think>")
    st.write(response)

