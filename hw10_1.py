import sqlite3
import datetime

def init_db():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            timestamp TEXT PRIMARY KEY,
            temperature REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_temperature(temp):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()
    cursor.execute('INSERT OR REPLACE INTO weather_data (timestamp, temperature) VALUES (?, ?)', (timestamp, temp))
    conn.commit()
    conn.close()
