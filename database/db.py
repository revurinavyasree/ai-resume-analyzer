import sqlite3
import hashlib
import os

DB_PATH = "database/resumes.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT NOT NULL,
            email    TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Resumes table linked to users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL,
            filename   TEXT NOT NULL,
            ats_score  INTEGER,
            skills     TEXT,
            uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
        """, (name, email, hash_password(password)))
        conn.commit()
        return True, "Registration successful."
    except sqlite3.IntegrityError:
        return False, "Email already registered."
    finally:
        conn.close()


def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users WHERE email = ? AND password = ?
    """, (email, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    if user:
        return True, dict(user)
    return False, "Invalid email or password."


def save_resume(user_id, filename, ats_score, skills):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO resumes (user_id, filename, ats_score, skills)
        VALUES (?, ?, ?, ?)
    """, (user_id, filename, ats_score, ", ".join(skills)))
    conn.commit()
    conn.close()


def get_user_resumes(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM resumes WHERE user_id = ?
        ORDER BY uploaded_at DESC
    """, (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_all_resumes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.*, u.name, u.email
        FROM resumes r
        JOIN users u ON r.user_id = u.id
        ORDER BY r.uploaded_at DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


# Auto-initialize DB on import
init_db()