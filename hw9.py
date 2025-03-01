import tkinter as tk
from tkinter import messagebox

class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate

    def convert_to_usd(self, amount_uah):
        return amount_uah / self.rate

def convert():
    try:
        amount_uah = float(entry_uah.get())
        amount_usd = converter.convert_to_usd(amount_uah)
        label_result.config(text=f"Еквівалент у доларах США: ${amount_usd:.2f}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректну числову суму в гривнях.")

official_rate = 41.5140
converter = CurrencyConverter(official_rate)

root = tk.Tk()
root.title("Конвертер валюти (UAH to USD)")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label_uah = tk.Label(frame, text="Сума в гривнях (UAH):")
label_uah.grid(row=0, column=0, pady=5)

entry_uah = tk.Entry(frame)
entry_uah.grid(row=0, column=1, pady=5)

button_convert = tk.Button(frame, text="Конвертувати", command=convert)
button_convert.grid(row=1, columnspan=2, pady=10)

label_result = tk.Label(frame, text="Еквівалент у доларах США: $0.00")
label_result.grid(row=2, columnspan=2, pady=5)

root.mainloop()
