from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  

# Define the pre-trained model to be used for text summarization
model_name = "facebook/bart-large-cnn"  # BART-based summarization model

# Load the model and tokenizer directly from the Hugging Face Hub
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("✅ Model loaded successfully from Hugging Face!")
