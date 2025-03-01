import tkinter as tk
import sqlite3

def get_last_temperature():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('SELECT temperature FROM weather_data ORDER BY timestamp DESC LIMIT 1')
    temp = cursor.fetchone()
    conn.close()
    return temp[0] if temp else "Немає даних"

def update_label():
    temp = get_last_temperature()
    label_temp.config(text=f"Остання температура: {temp}°C")
    root.after(10000, update_label)  # Оновлення кожні 10 сек

def start_gui():
    global root, label_temp
    root = tk.Tk()
    root.title("Температура")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    label_temp = tk.Label(frame, text="Остання температура: ...", font=("Arial", 14))
    label_temp.pack()

    update_label()  # Запускає оновлення GUI
    root.mainloop()
