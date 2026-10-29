"""SQLite database operations and progress tracking for JobMate AI."""

import sqlite3
from config import DB_PATH, PASS_PERCENTAGE
from quiz_data import QUIZ_LEVELS


def initialize_database(db_path=DB_PATH):
    """Ensure the quiz_results table exists."""
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS quiz_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quiz_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                total INTEGER NOT NULL,
                recommendation TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def save_quiz_result(quiz_name, score, total, recommendation, db_path=DB_PATH):
    """Record a completed quiz attempt into SQLite."""
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO quiz_results (quiz_name, score, total, recommendation)
            VALUES (?, ?, ?, ?)
            """,
            (quiz_name, score, total, recommendation),
        )


def get_latest_quiz_result(db_path=DB_PATH):
    """Fetch the most recent quiz attempt record."""
    with sqlite3.connect(db_path) as conn:
        return conn.execute(
            """
            SELECT quiz_name, score, total, recommendation, created_at
            FROM quiz_results
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()


def get_quiz_history(limit=10, db_path=DB_PATH):
    """Retrieve the most recent quiz results, up to the given limit."""
    with sqlite3.connect(db_path) as conn:
        return conn.execute(
            """
            SELECT id, quiz_name, score, total, recommendation, created_at
            FROM quiz_results
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()


def get_total_quiz_attempts(db_path=DB_PATH):
    """Count the total number of quiz submissions."""
    with sqlite3.connect(db_path) as conn:
        row = conn.execute("SELECT COUNT(*) FROM quiz_results").fetchone()
        return row[0] if row else 0


def get_best_percentage(quiz_name, db_path=DB_PATH):
    """Return the best saved percentage for a level, or 0.0 if never attempted."""
    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT MAX(CAST(score AS REAL) / total)
            FROM quiz_results
            WHERE quiz_name = ? AND total > 0
            """,
            (quiz_name,),
        ).fetchone()
    return row[0] if row and row[0] is not None else 0.0


def get_unlocked_levels(db_path=DB_PATH):
    """Unlock each next level after scoring at least 80% on the previous level."""
    unlocked = [QUIZ_LEVELS[0]["name"]]

    for level in QUIZ_LEVELS[1:]:
        previous_level = level["unlock_after"]
        if previous_level and get_best_percentage(previous_level, db_path=db_path) >= PASS_PERCENTAGE:
            unlocked.append(level["name"])
        else:
            # Progression is sequential; later levels cannot skip a locked level.
            break

    return unlocked


def get_recommendation(level_name, score, total):
    """Recommend practice based on the selected quiz level and score."""
    percentage = score / total if total else 0

    if percentage < 0.80:
        return (
            f"Review the explanations and retry {level_name}. "
            "Aim for at least 4/5 before moving on to a harder topic."
        )

    if level_name == "SQL Basics":
        return (
            "Great work on SQL Basics! You can practise Aggregation next, "
            "or retry Basics to improve your score."
        )
    if level_name == "SQL Aggregation":
        return (
            "Great work on Aggregation! You can practise Joins & Subqueries next, "
            "or retry this level to improve your score."
        )
    return (
        "Excellent work! You completed the Joins & Subqueries quiz. "
        "Practise these concepts on a real dataset or build a small SQL project."
    )
