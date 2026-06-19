import sqlite3
import hashlib
import secrets
import os

DB_PATH = "database/resumes.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    os.makedirs("database", exist_ok=True)

    conn = get_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Resumes Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        filename TEXT NOT NULL,

        ats_score REAL DEFAULT 0,
        jd_match REAL DEFAULT 0,

        skills TEXT,
        strengths TEXT,
        weaknesses TEXT,

        uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


# ----------------------------
# PASSWORD SECURITY
# ----------------------------

def hash_password(password):
    salt = secrets.token_hex(16)

    hashed = hashlib.sha256(
        (password + salt).encode()
    ).hexdigest()

    return f"{salt}${hashed}"


def verify_password(password, stored_password):
    try:
        salt, hashed = stored_password.split("$")

        check = hashlib.sha256(
            (password + salt).encode()
        ).hexdigest()

        return check == hashed

    except Exception:
        return False


# ----------------------------
# USER FUNCTIONS
# ----------------------------

def register_user(name, email, password):

    email = email.lower().strip()

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users
        (name, email, password)
        VALUES (?, ?, ?)
        """,
        (
            name.strip(),
            email,
            hash_password(password)
        ))

        conn.commit()

        return True, "Registration successful."

    except sqlite3.IntegrityError:
        return False, "Email already registered."

    except Exception as e:
        return False, str(e)

    finally:
        conn.close()


def login_user(email, password):

    email = email.lower().strip()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM users
    WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    if user and verify_password(
        password,
        user["password"]
    ):
        return True, dict(user)

    return False, "Invalid email or password."


def get_user_profile(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        name,
        email,
        created_at
    FROM users
    WHERE id = ?
    """, (user_id,))

    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


# ----------------------------
# RESUME FUNCTIONS
# ----------------------------

def save_resume(
    user_id,
    filename,
    ats_score,
    skills,
    jd_match=0,
    strengths="",
    weaknesses=""
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO resumes
    (
        user_id,
        filename,
        ats_score,
        jd_match,
        skills,
        strengths,
        weaknesses
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        user_id,
        filename,
        ats_score,
        jd_match,
        ", ".join(skills),
        strengths,
        weaknesses
    ))

    conn.commit()
    conn.close()


def get_user_resumes(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM resumes
    WHERE user_id = ?
    ORDER BY uploaded_at DESC
    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(r) for r in rows]


def get_all_resumes():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        r.*,
        u.name,
        u.email
    FROM resumes r
    JOIN users u
    ON r.user_id = u.id
    ORDER BY r.uploaded_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(r) for r in rows]


def get_best_resume(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM resumes
    WHERE user_id = ?
    ORDER BY ats_score DESC
    LIMIT 1
    """, (user_id,))

    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


def delete_resume(resume_id, user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM resumes
    WHERE id = ?
    AND user_id = ?
    """, (resume_id, user_id))

    conn.commit()
    conn.close()


# ----------------------------
# DASHBOARD STATISTICS
# ----------------------------

def get_user_statistics(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        COUNT(*) as total_resumes,
        ROUND(AVG(ats_score),2) as average_ats,
        MAX(ats_score) as best_ats
    FROM resumes
    WHERE user_id = ?
    """, (user_id,))

    stats = cursor.fetchone()

    conn.close()

    return dict(stats)


# ----------------------------
# AUTO INIT
# ----------------------------

init_db()