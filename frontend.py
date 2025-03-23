import streamlit as st  
import requests  
import base64  
import threading  
import uvicorn  
from fastapi import FastAPI  
from app import analyze  

# Initialize FastAPI inside Streamlit
app = FastAPI()

@app.get("/analyze")
async def analyze_route(company: str):
    """Fetch news, analyze sentiment, and generate Hindi TTS."""
    result = await analyze(company)
    return result

def run_api():
    """Run FastAPI inside a thread."""
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Run FastAPI in a background thread
threading.Thread(target=run_api, daemon=True).start()

# Streamlit UI
st.title("📢 AI-Powered News Summarization & Sentiment Analysis")
st.markdown("Enter a company name to fetch news, analyze sentiment, and generate Hindi TTS.")

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

                    if "error" in result:
                        st.error(f"⚠️ {result['error']}")
                    elif "articles" in result: 
                        st.subheader("📜 News Analysis Report")
                        for article in result["articles"]:
                            st.write(f"**📰 {article['title']}**")
                            st.write(f"📌 *Summary:* {article['summary']}")
                            st.write(f"💡 *Sentiment:* {article['sentiment']}")
                             
                        if "audio_base64" in result and result["audio_base64"]:
                            st.subheader("🔊 Hindi Audio Output")
                            audio_bytes = base64.b64decode(result["audio_base64"])
                            st.audio(audio_bytes, format="audio/mp3")
                            st.download_button(
                                label="Download Audio",
                                data=audio_bytes,
                                file_name="output.mp3",
                                mime="audio/mp3"
                            )
                        else:
                            st.warning("⚠️ No audio generated. TTS failed.")

                    else:
                        st.warning("⚠️ No articles found.")
                else:
                    st.error(f"⚠️ API Error: {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Connection Error: Backend server is not running.")
            except requests.exceptions.Timeout:
                st.error("⏳ Timeout Error: The request took too long.")
            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Failed to connect to API: {e}")
