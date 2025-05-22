import psycopg2

conn = psycopg2.connect(
    host="localhost", 
    database="resume_db",
    user="postgres",
    password="abhinav123",
    port="5432"
)
cursor = conn.cursor()
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            education TEXT,
            experience TEXT,
            analysis TEXT
        );
    """)
    conn.commit()

create_table()
def insert_data(name, email, phone, skills, education, experience, analysis):
    cursor.execute("""
        INSERT INTO resumes (name, email, phone, skills, education, experience, analysis)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (name, email, phone, skills, education, experience, analysis))
    conn.commit()
    create_table()