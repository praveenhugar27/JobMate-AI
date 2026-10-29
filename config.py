"""Configuration settings and constants for JobMate AI."""

# Ollama API settings
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"

# SQLite database file path
DB_PATH = "jobmate_progress.db"

# Minimum score percentage required to pass a quiz and unlock the next level
PASS_PERCENTAGE = 0.80

# Built-in keyword catalog for detecting skills in resumes and job descriptions
SKILLS = [
    "python", "sql", "excel", "power bi", "tableau", "pandas", "numpy",
    "statistics", "machine learning", "data analysis", "data visualization",
    "matplotlib", "communication", "java", "c++", "git", "html", "css",
    "javascript", "problem solving", "mysql", "postgresql", "deep learning",
    "aws",
]
