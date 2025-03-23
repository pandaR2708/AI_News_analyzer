import logging  # Logging for debugging
import os  # Handling environment variables
import httpx  # Async HTTP client for fetching news
from dotenv import load_dotenv  # Load environment variables from .env file
from fastapi import FastAPI, HTTPException  # FastAPI HTTP exception handling
from utils import generate_tts, analyze_sentiment, generate_summary  # Utility functions

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Get the NewsAPI key from environment variables
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Ensure API key is available
if not NEWS_API_KEY:
    logging.error("❌ NEWS_API_KEY is missing in environment variables.")
    raise Exception("Missing NEWS_API_KEY. Please add it to your environment variables.")

async def fetch_news(company):
    """
    Fetch news articles from NewsAPI based on the company name.

    Args:
        company (str): The name of the company to search news for.

    Returns:
        list: A list of dictionaries containing news titles and summaries.
    """
    if not company.strip():
        logging.error("❌ Company name is empty!")
        return [{"title": "Invalid Input", "summary": "Please enter a valid company name."}]

    # Construct the API request URL
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&apiKey={NEWS_API_KEY}"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

            # Check for API errors
            if response.status_code != 200:
                logging.error(f"❌ NewsAPI error {response.status_code}: {response.text}")
                return [{"title": "No news found", "summary": "Try another keyword"}]

            # Parse the API response JSON
            data = response.json()
            articles = data.get("articles", [])

            if not articles:
                logging.warning("⚠️ No articles found.")
                return [{"title": "No news found", "summary": "Try another keyword"}]

            # Process and return only the first 10 articles for efficiency
            return [{"title": item.get("title", "No Title"), "summary": item.get("description", "No Summary")}
                    for item in articles[:10]]

    except Exception as e:
        logging.error(f"❌ Error fetching news: {e}")
        return [{"title": "API Error", "summary": "Failed to fetch news. Try again later."}]

async def analyze(company: str):
    """
    Fetch news, analyze sentiment, and generate Hindi TTS.

    Args:
        company (str): The name of the company to analyze news for.

    Returns:
        dict: Dictionary containing processed articles and generated audio path.
    """
    
    # Fetch news articles
    news_articles = await fetch_news(company)

    # Ensure the response contains a list of articles
    if not isinstance(news_articles, list):
        raise HTTPException(status_code=500, detail="Invalid news data format.")

    processed_articles = []

    # Process each article
    for article in news_articles:
        if not isinstance(article, dict) or "summary" not in article:
            continue 

        # Generate a summarized version of the article
        summary = generate_summary(article["summary"])
        
        # Perform sentiment analysis on the summarized text
        sentiment = analyze_sentiment(summary)  

        # Append processed article data to the list
        processed_articles.append({
            "title": article.get("title", "No Title"),
            "summary": summary,
            "sentiment": sentiment
        })

    # If no valid articles were processed, return a message
    if not processed_articles:
        return {"message": "No valid news articles found."}

    # Generate Hindi text-to-speech audio for the articles
    audio_buffer = generate_tts(processed_articles)
    
    if audio_buffer is None:
        logging.warning("⚠️ TTS generation failed.")
        return {"articles": processed_articles, "audio_base64": None}

    import base64
    audio_base64 = base64.b64encode(audio_buffer.getvalue()).decode("utf-8")
    logging.info("✅ Hindi TTS successfully encoded to base64.")

    return {"articles": processed_articles, "audio_base64": audio_base64}
