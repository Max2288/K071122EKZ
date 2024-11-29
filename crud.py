import psycopg2
from typing import List

DB_SETTINGS = {
    "dbname": "school",
    "user": "user",
    "password": "password",
    "host": "localhost",
    "port": "5455",
}

def get_student_hobbies(student_id: int) -> List[dict]:
    conn = psycopg2.connect(**DB_SETTINGS)
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT hobbies.id, hobbies.name
                FROM hobbies
                JOIN student_hobbies ON hobbies.id = student_hobbies.hobby_id
                WHERE student_hobbies.student_id = %s;
            """, (student_id,))
            return [{"id": row[0], "name": row[1]} for row in cur.fetchall()]
    finally:
        conn.close()

def delete_student(student_id: int):
    conn = psycopg2.connect(**DB_SETTINGS)
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE id = %s;", (student_id,))
        conn.commit()
    finally:
        conn.close()

def add_student(name: str) -> int:
    conn = psycopg2.connect(**DB_SETTINGS)
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO students (name) VALUES (%s) RETURNING id;", (name,))
            student_id = cur.fetchone()[0]
        conn.commit()
        return student_id
    finally:
        conn.close()

def add_hobby(name: str):
    conn = psycopg2.connect(**DB_SETTINGS)
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO hobbies (name) VALUES (%s) RETURNING id;", (name,))
            hobby_id = cur.fetchone()[0]
        conn.commit()
        return hobby_id
    except Exception:
        conn.rollback()
        raise ValueError(f"Hobby with name '{name}' already exists.")
    finally:
        conn.close()

def assign_hobby_to_student(student_id: int, hobby_id: int):
    conn = psycopg2.connect(**DB_SETTINGS)
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO student_hobbies (student_id, hobby_id)
                VALUES (%s, %s);
            """, (student_id, hobby_id))
        conn.commit()
    except Exception:
        conn.rollback()
        raise ValueError(f"Student {student_id} already has hobby {hobby_id}.")
    finally:
        conn.close()
