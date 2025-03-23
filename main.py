from fastapi import FastAPI, HTTPException  
from app import analyze  
import os  
import logging  
import base64  

logging.basicConfig(level=logging.INFO)  # Set logging level to info

# Load News API Key from environment variables
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    logging.error("❌ NEWS_API_KEY is missing.")
    raise Exception("Missing NEWS_API_KEY.")

# Initialize FastAPI application
app = FastAPI()

@app.get("/analyze")
async def analyze_route(company: str):
    """
    API endpoint to fetch news, analyze sentiment, and generate Hindi TTS.

    Args:
        company (str): Company name to analyze.

    Returns:
        dict: Contains articles, summaries, sentiment analysis, and audio.
    """
    try:
        result = await analyze(company)
        
        # Convert generated TTS audio to base64
        if "audio_path" in result and result["audio_path"]:
            audio_buffer = result["audio_path"]
            audio_base64 = base64.b64encode(audio_buffer.read()).decode("utf-8")
            
            return {
                "articles": result["articles"],
                "audio_base64": audio_base64
            }

        return result
    except Exception as e:
        logging.error(f"❌ Error processing request: {e}")
        return {"error": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
