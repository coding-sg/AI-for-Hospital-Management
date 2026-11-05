import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import prompt
from schemas import HospitalManagementResponse

load_dotenv()

def get_llm():
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("MODEL_NAME") or "gemini-3.5-flash"

    if not api_key:
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            api_key = None

    try:
        configured_model = st.secrets.get("MODEL_NAME")
        if configured_model:
            model_name = configured_model
    except Exception:
        pass

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing. Add it to .env or Streamlit Cloud Secrets.")

    return ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=api_key,
        temperature=0.2,
    )

def generate_hospital_management_answer(
    question, topic, knowledge_level, response_style,
    include_examples=True, include_metrics=True,
    include_checklist=True, extra_context=""
):
    llm = get_llm()
    structured_llm = llm.with_structured_output(HospitalManagementResponse)
    chain = prompt | structured_llm
    return chain.invoke({
        "question": question,
        "topic": topic,
        "knowledge_level": knowledge_level,
        "response_style": response_style,
        "include_examples": include_examples,
        "include_metrics": include_metrics,
        "include_checklist": include_checklist,
        "extra_context": extra_context or "No additional context provided.",
    })
