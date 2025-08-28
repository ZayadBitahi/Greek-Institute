import psycopg2

conn = psycopg2.connect(
    "postgresql://neondb_owner:npg_eLjKPms67crx@ep-falling-art-a2ygx9t8-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)
cursor = conn.cursor()