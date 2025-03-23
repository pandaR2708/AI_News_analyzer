---
title: AI-Powered News Summarization & Sentiment Analysis
emoji: 📰
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.30.0
app_file: frontend.py
pinned: false
---

## 💟 AI-Powered News Summarization & Sentiment Analysis

This project fetches news articles based on a company name, generates summaries, performs sentiment analysis, and converts the summarized news into Hindi text-to-speech (TTS).

---

## 📂 Project Structure
```
├── app.py          # Main logic for fetching news, summarizing, and sentiment analysis
├── frontend.py     # Streamlit-based frontend
├── main.py         # FastAPI backend (if needed)
├── model.py        # Loads the Hugging Face summarization model
├── requirements.txt # Lists all dependencies
├── utils.py        # Utility functions (sentiment analysis, summarization, TTS)
├── Dockerfile      # Optional: Containerization for deployment
└── README.md       # Project documentation
```

---

## 🌟 Features
- 📰 **Fetches News Articles**: Retrieves real-time news from NewsAPI.
- 🧠 **Summarizes News**: Uses a **transformer-based model** for concise summaries.
- 🎭 **Sentiment Analysis**: Classifies news sentiment as **Positive, Neutral, or Negative**.
- 🔊 **Hindi Text-to-Speech (TTS)**: Converts summaries into **Hindi audio** using gTTS.
- 🎨 **User-Friendly UI**: Streamlit-based interactive web app.
- ⚡ **FastAPI Backend** (Optional): API for news processing & AI-driven analytics.

---

## 🛠 Installation

### 🔹 Prerequisites
- **Python 3.11+**
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### 🔹 Setup Environment Variables
1. **Get a NewsAPI key** from [NewsAPI.org](https://newsapi.org/).
2. Create a `.env` file in the project root:
   ```
   NEWS_API_KEY=your_news_api_key_here
   ```

---

## 🚀 Running the Application

### 🔹 Start the Backend (FastAPI)
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
API available at: [http://127.0.0.1:8000/analyze](http://127.0.0.1:8000/analyze)

### 🔹 Start the Frontend (Streamlit UI)
```sh
streamlit run frontend.py
```
UI available at: [http://localhost:8501](http://localhost:8501)

---

## 🛠 API Endpoints
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

## 💾 Deployment on Hugging Face Spaces

### 🔹 1. Create a Hugging Face Space
- Go to [Hugging Face Spaces](https://huggingface.co/spaces).
- Click `Create New Space`.
- Select `SDK: Streamlit`.

### 🔹 2. Push Code to Hugging Face
```sh
git add .
git commit -m "Deploying to Hugging Face"
git push origin main
```

### 🔹 3. Configure `README.md` for Hugging Face
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

### 🔹 4. Deploy & Run
- The app will be available at: `https://huggingface.co/spaces/AI_News_Analyzer`

---

## 📂 GitHub Repository
[GitHub Repository](https://github.com/pandaR2708/AI_News_analyzer)

---

## 📊 Optimizations
- ✅ **Fixed deep-translator issue** (Use version `1.11.4` or `1.11.9`).
- ✅ **Optimized article fetching with `asyncio` to reduce processing time**.
- ✅ **Tested locally before deploying**.

---

## 💬 Contributing
- **Fork** the repository
- **Create a feature branch** (`git checkout -b feature-new`)
- **Commit changes** (`git commit -m "Added new feature"`)
- **Push changes** (`git push origin feature-new`)
- **Submit a Pull Request**

We welcome contributions from the community! 🚀  

---

## 📞 Contact
📧 Email: `shivam.ranjan16@gmail.com`

