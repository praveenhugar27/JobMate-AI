# 🎯 JobMate AI - Your Personal Placement Strategist

JobMate AI is a Streamlit application powered by local LLMs (Ollama) and SQLite to analyze resume skill gaps against job descriptions, generate customized preparation schedules, and run interactive interview readiness quizzes.

---

## 📁 Modular Project Structure

```text
JobMate-AI/
├── app.py                # Main Streamlit application entry point & layout
├── config.py             # System constants, model parameters, skill catalog
├── quiz_data.py          # SQL & Role-based question banks
├── database.py           # SQLite database schema, history & score tracking
├── services.py           # PyMuPDF resume parsing, regex skill detection, Ollama API
├── ui_components.py      # Modular Streamlit UI sections (Readiness, Quizzes, History)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 Quickstart

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Ensure Ollama is Running
Make sure Ollama is installed and running with your target model:
```bash
ollama run qwen2.5:3b
```

### 3. Launch the App
```bash
streamlit run app.py
```
