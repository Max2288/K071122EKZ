import psycopg2

DB_SETTINGS = {
    "dbname": "school",
    "user": "user",
    "password": "password",
    "host": "localhost",
    "port": "5455",
}

CREATE_TABLES = """
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS hobbies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS student_hobbies (
    student_id INT NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    hobby_id INT NOT NULL REFERENCES hobbies(id) ON DELETE CASCADE,
    UNIQUE (student_id, hobby_id)
);
"""


def apply_migrations():
    conn = psycopg2.connect(**DB_SETTINGS)
    try:
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLES)
        conn.commit()
    finally:
        conn.close()

if __name__ == "__main__":
    apply_migrations()
