import streamlit as st
import requests
from bs4 import BeautifulSoup
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"


def fetch_html(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=8)
        return response.text if response.status_code == 200 else None
    except:
        return None


def extract_main_text(html):
    soup = BeautifulSoup(html, "lxml")

    texts = []
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3']):
        text = tag.get_text(strip=True)
        if text and len(text) > 50 and "cookie" not in text.lower():
            texts.append(text)

    return " ".join(texts)[:1200]


def clean_output(output):
    output = output.strip()
    if output.startswith("```"):
        parts = output.split("```")
        if len(parts) >= 2:
            output = parts[1]
    return output.strip()


def generate_summary(text):
    prompt = f"""
You are a venture capitalist analyzing a startup website.

Extract only what can be inferred. No hallucination.

Return JSON:
{{
  "one_liner": "...",
  "problem": "...",
  "solution": "...",
  "target_customers": "...",
  "business_model": "...",
  "moat": "..."
}}

Content:
{text}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 1000,
            "temperature": 0.3
        }
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    return clean_output(response.json().get("response", ""))


# ---------------- UI ---------------- #

st.set_page_config(page_title="VC Startup Analyzer", layout="centered")

st.title("🚀 VC Startup Analyzer")
st.write("Paste a startup URL and get a VC-style summary")

url = st.text_input("Enter website URL")

if st.button("Analyze"):
    if not url:
        st.warning("Please enter a URL")
    else:
        with st.spinner("Analyzing..."):
            html = fetch_html(url)

            if not html:
                st.error("Failed to fetch website")
            else:
                text = extract_main_text(html)
                summary = generate_summary(text)

                try:
                    data = json.loads(summary)

                    st.subheader("📊 VC Summary")

                    st.write("**One-liner:**", data.get("one_liner"))
                    st.write("**Problem:**", data.get("problem"))
                    st.write("**Solution:**", data.get("solution"))
                    st.write("**Target Customers:**", data.get("target_customers"))
                    st.write("**Business Model:**", data.get("business_model"))
                    st.write("**Moat:**", data.get("moat"))

                except:
                    st.error("Could not parse response")
                    st.text(summary)