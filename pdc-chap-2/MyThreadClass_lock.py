import math
import threading
import time
import os
from threading import Thread
from random import randint, uniform

# =========================
# Weather Calculations
# =========================
def weather_calculations():
    temperature = uniform(20, 40)   # °C
    humidity = uniform(30, 90)      # %
    wind_speed = uniform(5, 25)     # km/h
    pressure = uniform(950, 1050)   # hPa

    heat_index = temperature + 0.33 * humidity - 0.7 * wind_speed - 4
    dew_point = temperature - ((100 - humidity) / 5)
    comfort_level = (100 - abs(temperature - 25)) + (humidity / 2) - (wind_speed / 3)
    total = heat_index + dew_point + comfort_level + pressure

    return total


# =========================
# Lock Definition
# =========================
threadLock = threading.Lock()


# =========================
# Thread Class
# =========================
class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Perform weather calculation
        result = weather_calculations()

        # Acquire the Lock for printing
        threadLock.acquire()
        print(f"---> {self.name} running, Process ID: {os.getpid()}")
        print(f"Weather Result = {result:.2f}")
        threadLock.release()

        time.sleep(self.duration)

        # Acquire lock again for finish message
        threadLock.acquire()
        print(f"---> {self.name} Finished\n")
        threadLock.release()


# =========================
# Main Function
# =========================
def main():
    start_time = time.time()

    # Creating Threads
    threads = []
    for i in range(1, 10):
        t = MyThreadClass(f"Thread#{i}", randint(1, 5))
        threads.append(t)

    # Starting Threads
    for t in threads:
        t.start()

    # Joining Threads
    for t in threads:
        t.join()

    print("End")
    print(f"--- {time.time() - start_time} seconds ---")


if __name__ == "__main__":
    main()
