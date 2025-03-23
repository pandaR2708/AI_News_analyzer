import logging  
import os  
import httpx  
import asyncio
from dotenv import load_dotenv  
from fastapi import FastAPI, HTTPException  
from utils import generate_tts, analyze_sentiment, generate_summary  

logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
if not NEWS_API_KEY:
    logging.error("❌ NEWS_API_KEY is missing in environment variables.")
    raise Exception("Missing NEWS_API_KEY.")

async def fetch_news(company):
    """Fetch news articles from NewsAPI asynchronously."""
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&apiKey={NEWS_API_KEY}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            logging.error(f"❌ NewsAPI error {response.status_code}: {response.text}")
            return []
        data = response.json()
        return [{"title": a.get("title", "No Title"), "summary": a.get("description", "No Summary")} for a in data.get("articles", [])[:10]]

async def analyze(company: str):
    """Fetch news, generate summaries, analyze sentiment, and create Hindi TTS."""
    news_articles = await fetch_news(company)

    if not news_articles:
        return {"message": "No news found."}

    summaries = await asyncio.gather(*(generate_summary(a["summary"]) for a in news_articles))
    sentiments = await asyncio.gather(*(analyze_sentiment(s) for s in summaries))

    processed_articles = [
        {"title": news_articles[i]["title"], "summary": summaries[i], "sentiment": sentiments[i]}
        for i in range(len(news_articles))
    ]

    audio_buffer = generate_tts(processed_articles)
    if audio_buffer:
        import base64
        audio_base64 = base64.b64encode(audio_buffer.getvalue()).decode("utf-8")
        return {"articles": processed_articles, "audio_base64": audio_base64}

    return {"articles": processed_articles, "audio_base64": None}
