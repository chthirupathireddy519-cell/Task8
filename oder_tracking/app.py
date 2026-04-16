from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Th@939070",
        database="order_tracking"
    )

@app.route('/')
def report():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Fetch summary (view)
    cursor.execute("SELECT * FROM daily_order_report")
    summary = cursor.fetchall()

    # Fetch detailed logs
    cursor.execute("SELECT * FROM order_log ORDER BY changed_at DESC")
    logs = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("report.html", summary=summary, logs=logs)

if __name__ == "__main__":
    app.run(debug=True)