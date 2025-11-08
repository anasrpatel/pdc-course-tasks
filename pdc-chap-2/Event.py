import math
import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

weather_data = []
event = threading.Event()

# ========================
# Weather Calculations
# ========================
def weather_calculations():
    temperature = random.uniform(20, 40)   # °C
    humidity = random.uniform(30, 90)      # %
    wind_speed = random.uniform(5, 25)     # km/h
    pressure = random.uniform(950, 1050)   # hPa

    heat_index = temperature + 0.33 * humidity - 0.7 * wind_speed - 4
    dew_point = temperature - ((100 - humidity) / 5)
    comfort_level = (100 - abs(temperature - 25)) + (humidity / 2) - (wind_speed / 3)
    total = heat_index + dew_point + comfort_level + pressure

    return total


# ========================
# Multithreading Classes
# ========================
class Consumer(threading.Thread):
    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            if weather_data:
                data = weather_data.pop()
                logging.info(f'Consumer notify: Weather result {data:.2f} popped by {self.name}')


class Producer(threading.Thread):
    def run(self):
        for i in range(5):   
            time.sleep(2)
            result = weather_calculations()   
            weather_data.append(result)
            logging.info(f'Producer notify: Calculated weather total {result:.2f} appended by {self.name}')
            event.set()
            event.clear()


# ========================
# Main Execution
# ========================
if __name__ == "__main__":
    t1 = Producer(name='Producer')
    t2 = Consumer(name='Consumer')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
