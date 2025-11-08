import math
import threading
import time
import random

# =============================
# Weather Calculations
# =============================
def weather_calculations():
    # Simulated weather data parameters
    temperature = 30.5
    humidity = 68
    wind_speed = 14.8
    pressure = 1012.3

    # Perform some mathematical weather-related computations
    heat_index = temperature + 0.1 * humidity - (wind_speed * 0.2)
    comfort_level = (temperature + humidity / 10) - (pressure / 1000)
    forecast_value = (temperature * 2 + humidity * 0.3) - (wind_speed / 5)

    total = heat_index + comfort_level + forecast_value
    return total


# =============================
# Weather Box with RLock
# =============================
class WeatherBox:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_data = 0

    def execute(self, value):
        with self.lock:
            # Perform weather calculation each time data is added/removed
            w_result = weather_calculations()
            self.total_data += value
            print(f"Weather Total = {w_result:.2f} | Current Records = {self.total_data}")

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)


# =============================
# Thread Functions
# =============================
def adder(box, records):
    print(f"N° {records} weather records to ADD\n")
    while records:
        box.add()
        time.sleep(1)
        records -= 1
        print(f"ADDED one record --> {records} left to ADD\n")


def remover(box, records):
    print(f"N° {records} weather records to REMOVE\n")
    while records:
        box.remove()
        time.sleep(1)
        records -= 1
        print(f"REMOVED one record --> {records} left to REMOVE\n")


# =============================
# Main Function
# =============================
def main():
    box = WeatherBox()

    t1 = threading.Thread(target=adder, args=(box, random.randint(10, 20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1, 10)))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


# =============================
# Entry Point
# =============================
if __name__ == "__main__":
    main()
