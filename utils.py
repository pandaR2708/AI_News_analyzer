import io  
import logging  
import asyncio
from deep_translator import GoogleTranslator  
from gtts import gTTS  
from textblob import TextBlob  
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  
import torch  

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load summarization model and tokenizer
model_name = "facebook/bart-large-cnn"
device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)
logging.info("✅ Model loaded successfully!")

async def analyze_sentiment(summary):
    """Perform sentiment analysis asynchronously."""
    try:
        blob = TextBlob(summary)
        polarity = blob.sentiment.polarity
        return "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        return "Neutral"

async def generate_summary(text):
    """Generate summaries in batches to improve efficiency."""
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(device)
        summary_ids = model.generate(inputs.input_ids, max_length=150, min_length=50, num_beams=4, early_stopping=True)
        return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        logging.error(f"Error generating summary: {e}")
        return "Summary generation failed."

def generate_tts(news_articles):
    """Convert summarized articles to Hindi speech and save as a file."""
    try:
        full_summary = " ".join([f"{a['title']}: {a['summary']} (Sentiment: {a['sentiment']})." for a in news_articles])
        translated_text = GoogleTranslator(source="en", target="hi").translate(full_summary)
        tts = gTTS(text=translated_text, lang="hi")

        # Save audio file
        audio_path = "output.mp3"
        tts.save(audio_path)

        return audio_path  # Return file path
    except Exception as e:
        logging.error(f"❌ Error generating TTS: {e}")
        return None
