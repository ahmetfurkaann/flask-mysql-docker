import time
from flask import Flask, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

app = Flask(__name__)

# .env içindeki MySQL bağlantı bilgilerini oku
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}


def get_mysql_connection():
    """ MySQL bağlantısını belirli bir süre boyunca dene """
    for _ in range(5):  # 5 kez tekrar dene
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            return conn
        except mysql.connector.Error as e:
            print(f"MySQL bağlantı hatası: {e}. Tekrar deneniyor...")
            time.sleep(5)  # 5 saniye bekle ve tekrar dene
    return None  # Bağlantı başarısız olursa None döndür

def get_kisiler():
    """ MySQL'den kisiler tablosundaki tüm verileri çeker """
    try:
        conn = get_mysql_connection()
        if conn is None:
            return {"error": "MySQL bağlantısı kurulamadı"}

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM kisiler")
        kisiler = cursor.fetchall()

        cursor.close()
        conn.close()
        
        return kisiler
    except Exception as e:
        return {"error": str(e)}

@app.route('/kisiler', methods=['GET'])
def kisiler():
    """ API endpoint - kisiler tablosundaki verileri döndürür """
    return jsonify(get_kisiler())


@app.route('/')
def hello():
    return "hello index"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
