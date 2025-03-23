from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  
import torch

# Define the pre-trained model to be used for text summarization
model_name = "facebook/bart-large-cnn"

# Load the model and tokenizer, use GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("✅ Model loaded successfully from Hugging Face!")
