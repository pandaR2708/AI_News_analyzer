import io  # Handles in-memory file objects
import logging  # Logging for debugging
from deep_translator import GoogleTranslator  # Translates English to Hindi
from gtts import gTTS  # Converts text to speech
from textblob import TextBlob  # Sentiment analysis
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  # Hugging Face models
import torch  # Required for model execution

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

# Load pre-trained summarization model from Hugging Face
model_name = "facebook/bart-large-cnn"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
logging.info("✅ Model loaded successfully!")

def analyze_sentiment(summary):
    """
    Perform sentiment analysis on the given summary using TextBlob.

    Args:
        summary (str): The summarized text.

    Returns:
        str: Sentiment label - 'Positive', 'Negative', or 'Neutral'.
    """
    try:
        blob = TextBlob(summary)  # Process text for sentiment analysis
        polarity = blob.sentiment.polarity  # Get sentiment polarity (-1 to 1)

        # Categorize polarity into Positive, Negative, or Neutral sentiment
        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        return "Neutral"  # Default sentiment if an error occurs

def generate_summary(text):
    """
    Generate a concise summary from the given text using a transformer model.

    Args:
        text (str): The input text to summarize.

    Returns:
        str: The generated summary.
    """
    try:
        # Dynamically determine the summary length based on input text size
        input_length = len(text.split())
        max_length = min(256, max(80, int(input_length * 0.5)))  
        min_length = max(50, max (25, int(max_length * 0.6)))  

        # Tokenize input text and generate summary using the transformer model
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        summary_ids = model.generate(
            inputs.input_ids, 
            max_length=max_length, 
            min_length=min_length, 
            num_beams=4,  
            early_stopping=True
        )
        
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        logging.error(f"Error generating summary: {e}")
        return "Summary generation failed."

def generate_tts(news_articles):
    """
    Convert summarized news articles into Hindi speech using Google TTS.
    """
    try:
        logging.info("🔍 Generating Hindi TTS...")

        # Combine multiple articles into one text
        full_summary = " ".join([
            f"{article['title']}: {article['summary']} (Sentiment: {article['sentiment']})."
            for article in news_articles
        ])

        if not full_summary.strip():
            logging.warning("⚠️ No text provided for TTS generation!")
            return None

        logging.info(f"📝 Text for TTS (before translation): {full_summary}")

        # Translate to Hindi
        translated_text = GoogleTranslator(source="en", target="hi").translate(full_summary)

        logging.info(f"🔤 Translated Hindi Text: {translated_text}")

        # Convert text to speech (Hindi)
        tts = gTTS(text=translated_text, lang="hi")
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)

        logging.info("✅ Hindi TTS generated successfully!")
        return audio_buffer  # Return generated audio buffer
    except Exception as e:
        logging.error(f"❌ Error generating TTS: {e}")
        return None
