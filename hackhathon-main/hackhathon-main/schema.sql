-- schema.sql
CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    skills TEXT[],
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
