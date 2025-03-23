---
title: AI-Powered News Summarization & Sentiment Analysis
emoji: 📰
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.43.2
app_file: frontend.py
pinned: false
---

## 📢 AI-Powered News Summarization & Sentiment Analysis

This project fetches news articles based on a company name, generates summaries, performs sentiment analysis, and converts the summarized news into Hindi text-to-speech (TTS).

---

## 📂 Project Structure
├── app.py # Main logic for fetching news, summarizing, and sentiment analysis and integrating all the files
├── frontend.py # Streamlit-based frontend with embedded FastAPI backend
├── main.py # Logic for Fast API and backend
├── model.py # Loads the Hugging Face summarization model
├── requirements.txt # Lists all dependencies
├── utils.py # Utility functions for sentiment analysis, summarization, and TTS
└── README.md # Project documentation

---
## 🌟 Features
- 📰 **Fetches News Articles**: Retrieves real-time news data from NewsAPI.
- 🧠 **Summarizes News**: Uses a **transformer-based model** for concise summaries.
- 🎭 **Sentiment Analysis**: Classifies news sentiment as **Positive, Neutral, or Negative**.
- 🔊 **Hindi Text-to-Speech (TTS)**: Converts summaries into **Hindi audio** using gTTS.
- 🎨 **User-Friendly UI**: Provides an interactive **Streamlit-based web app**.
- ⚡ **FastAPI Backend**: API support for news processing and AI-driven analytics.

---

## 🛠 Installation
### 🔹 Prerequisites
- Ensure **Python 3.11+** is installed.
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### 🔹 Setup Environment Variables
1. **Get a NewsAPI key** from [NewsAPI.org](https://newsapi.org/).
2. Create a `.env` file in the project root and add:
   ```
   NEWS_API_KEY=your_news_api_key_here
   ```

---

## 🚀 Running the Application
### 🔹 Start the Backend (FastAPI Server)
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
- The API will be available at: [http://127.0.0.1:8000/analyze](http://127.0.0.1:8000/analyze)

### 🔹 Start the Frontend (Streamlit UI)
```sh
streamlit run frontend.py
```
- Access the UI at: [http://localhost:8501](http://localhost:8501)

---

## 🔗 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/analyze?company=Apple` | Fetches news, summarizes content, analyzes sentiment, and generates TTS |

### 🔹 Example API Response
```json
{
  "articles": [
    {
      "title": "Apple stock surges",
      "summary": "Apple shares hit a record high...",
      "sentiment": "Positive"
    }
  ],
  "audio_base64": "base64_encoded_audio_string"
}
```

---

## 🎨 Deployment on Hugging Face Spaces
### 🔹 1️⃣ Create a Hugging Face Space
- Go to [Hugging Face Spaces](https://huggingface.co/spaces).
- Click `Create New Space`.
- Select `SDK: Streamlit`.

### 🔹 2️⃣ Push Code to Hugging Face
```sh
git add .
git commit -m "Deploying to Hugging Face"
git push origin main
```

### 🔹 3️⃣ Configure `README.md` for Hugging Face
Replace `README.md` with:
```yaml
---
title: AI News Summarization
emoji: 📰
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.30.0"
app_file: frontend.py
pinned: false
---
```
---

## 🔹 📂 Git hub Repository Link:
https://github.com/pandaR2708/AI_News_analyzer

---

### 🌟 Before Deploying:
- Ensure you have a valid NewsAPI key. Create a `.env` file in the project root and add: NEWS_API_KEY=your_news_api_key_here

---

### 🔹 4️⃣ Deploy & Run
- The app will be available at: `https://huggingface.co/spaces/AI_News_Analyzer`

---

📌 Feel free to modify, improve, and contribute!

---

## 💡 Contributing
✅ **Fork** the repository  
✅ **Create a feature branch** (`git checkout -b feature-new`)  
✅ **Commit changes** (`git commit -m "Added new feature"`)  
✅ **Push changes** (`git push origin feature-new`)  
✅ **Submit a Pull Request**  

We welcome contributions from the community! 🚀  

---

## 📞 Contact
📧 Email: `shivam.ranjan16@gmail.com`  