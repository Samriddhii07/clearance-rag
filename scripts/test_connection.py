import os
import psycopg
import redis
from dotenv import load_dotenv

load_dotenv()

#---------- Postgres ----------
conn = psycopg.connect(
    host="localhost",
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)
print("Postgres connected!")

cur = conn.cursor()

cur.execute("SELECT version();")
print("Version:", cur.fetchone()[0])

cur.execute("SELECT '[1,2,3]'::vector <=> '[1,2,4]'::vector;")
print("Cosine distance:", cur.fetchone()[0])

cur.close()
conn.close()

# ---------- Redis ----------
r = redis.Redis(
    host="localhost",
    port=int(os.getenv("REDIS_PORT")),
    decode_responses=True,
)
r.set("hello", "world")
print("Redis value:", r.get("hello"))
r.close()