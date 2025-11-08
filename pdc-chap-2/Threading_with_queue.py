import math
from threading import Thread
from queue import Queue
from random import uniform
import time

# =======================
# Weather Data Simulation
# =======================
def weather_data_simulation():
    temperature = uniform(20, 40)   # °C
    humidity = uniform(30, 90)      # %
    wind_speed = uniform(5, 25)     # km/h
    pressure = uniform(950, 1050)   # hPa

    # Basic weather calculations
    heat_index = temperature + 0.33 * humidity - 0.7 * wind_speed - 4
    dew_point = temperature - ((100 - humidity) / 5)
    comfort_level = (100 - abs(temperature - 25)) + (humidity / 2) - (wind_speed / 3)

    total = heat_index + dew_point + comfort_level + pressure
    return total


# =======================
# Producer - Consumer Code
# =======================
class Producer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            result = weather_data_simulation()
            self.queue.put(result)
            print(f"Producer notify: Weather calculation result {result:.2f} added to queue by {self.name}")
            time.sleep(1)


class Consumer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            result = self.queue.get()
            print(f"Consumer notify: Weather result {result:.2f} processed by {self.name}")
            self.queue.task_done()


# =======================
# Main Program
# =======================
if __name__ == '__main__':
    queue = Queue()

    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
