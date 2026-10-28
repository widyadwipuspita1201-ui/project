import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash

# Sesuaikan dengan pengaturan MySQL XAMPP di komputer Anda.
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "siakad",
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def setup_login():
    """Membuat tabel pengguna jika belum ada dan menambahkan akun demo."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pengguna (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL,
                nama VARCHAR(150) NOT NULL
            )
        """)
        conn.commit()
        cursor.execute("SELECT id FROM pengguna WHERE username=%s", ("admin",))
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO pengguna (username, password_hash, nama) VALUES (%s, %s, %s)",
                ("admin", generate_password_hash("admin123"), "Administrator")
            )
            conn.commit()
    finally:
        cursor.close()
        conn.close()

def check_login(username, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT id, username, password_hash, nama FROM pengguna WHERE username=%s",
            (username,)
        )
        user = cursor.fetchone()
        if user and check_password_hash(user["password_hash"], password):
            user.pop("password_hash", None)
            return user
        return None
    finally:
        cursor.close()
        conn.close()
