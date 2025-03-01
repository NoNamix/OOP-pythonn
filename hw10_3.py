import threading
import time
from hw10_1 import init_db
from hw10 import update_weather_data
from hw10_2 import start_gui


def background_update():
    while True:
        update_weather_data()
        time.sleep(1800)


if __name__ == "__main__":
    init_db()

    weather_thread = threading.Thread(target=background_update, daemon=True)
    weather_thread.start()

    start_gui()
