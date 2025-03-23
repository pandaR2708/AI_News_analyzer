import streamlit as st  
import requests  
import base64  
import threading  
import uvicorn  
from fastapi import FastAPI  
from app import analyze  

app = FastAPI()

@app.get("/analyze")
async def analyze_route(company: str):
    """Fetch news, analyze sentiment, and generate Hindi TTS."""
    return await analyze(company)

def run_api():
    """Run FastAPI inside a thread."""
    uvicorn.run(app, host="0.0.0.0", port=8000)

threading.Thread(target=run_api, daemon=True).start()

st.title("📢 AI-Powered News Summarization & Sentiment Analysis")
company_name = st.text_input("🔍 Enter Company Name", "")

if st.button("Fetch News & Analyze"):
    if not company_name.strip():
        st.warning("⚠️ Please enter a valid company name!")
    else:
        with st.spinner("Fetching and analyzing news..."):
            try:
                response = requests.get("http://0.0.0.0:8000/analyze", params={"company": company_name})

                if response.status_code == 200:
                    result = response.json()
                    for article in result.get("articles", []):
                        st.write(f"**📰 {article['title']}**")
                        st.write(f"📌 *Summary:* {article['summary']}")
                        st.write(f"💡 *Sentiment:* {article['sentiment']}")

                    if result.get("audio_base64"):
                        audio_bytes = base64.b64decode(result["audio_base64"])
                        st.audio(audio_bytes, format="audio/mp3")
                        st.download_button("Download Audio", audio_bytes, "output.mp3", "audio/mp3")
                else:
                    st.error(f"⚠️ API Error: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Failed to connect to API: {e}")
