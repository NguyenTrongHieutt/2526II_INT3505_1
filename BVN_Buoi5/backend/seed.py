import psycopg2
from faker import Faker
import random

fake = Faker()

conn = psycopg2.connect(
    host="db",
    database="pagination",
    user="postgres",
    password="postgres"
) 

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    created_at TIMESTAMP
)
""")
cur.execute("CREATE INDEX IF NOT EXISTS idx_users_id ON users(id)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)")

conn.commit()

TOTAL = 1_000_000
BATCH = 5000

for i in range(0, TOTAL, BATCH):

    records = []

    for _ in range(BATCH):
        records.append((
            fake.name(),
            fake.email(),
            fake.date_time()
        ))

    cur.executemany(
        "INSERT INTO users(name,email,created_at) VALUES(%s,%s,%s)",
        records
    )

    conn.commit()

    print("Inserted:", i)

print("DONE")