import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1234"
    )

    print("✅ Connected:", conn.open)

    with conn.cursor() as cursor:
        cursor.execute("SHOW DATABASES")
        for db in cursor.fetchall():
            print(db[0])

except Exception as e:
    print("❌ Error:", e)
