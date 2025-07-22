import sqlite3

DB_PATH = "db/ecommerce.db"

def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()
