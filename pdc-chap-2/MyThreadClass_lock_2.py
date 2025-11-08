import math
import threading
import time
import os
from threading import Thread
from random import randint, uniform

# ====================================
# Weather Calculations Function
# ====================================
def weather_calculations():
    # Simulated random weather readings
    temperature = uniform(20, 40)    # °C
    humidity = uniform(30, 90)       # %
    wind_speed = uniform(5, 25)      # km/h
    pressure = uniform(950, 1050)    # hPa

    # Weather formula calculations
    heat_index = temperature + 0.33 * humidity - 0.7 * wind_speed - 4
    dew_point = temperature - ((100 - humidity) / 5)
    comfort_index = (100 - abs(temperature - 25)) + (humidity / 2) - (wind_speed / 3)

    total = heat_index + dew_point + comfort_index + pressure
    return total


# ====================================
# Lock Definition
# ====================================
threadLock = threading.Lock()


# ====================================
# Thread Class
# ====================================
class WeatherThread(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Acquire lock before printing
        threadLock.acquire()
        print(f"---> {self.name} running, PID = {os.getpid()}")
        threadLock.release()

        # Perform Weather Calculations
        result = weather_calculations()
        print(f"{self.name} Result of Weather Calculations = {result:.2f}")

        time.sleep(self.duration)
        print(f"---> {self.name} finished.\n")


# ====================================
# Main Function
# ====================================
def main():
    start_time = time.time()

    # Thread Creation
    threads = [WeatherThread(f"Thread#{i} ", randint(1, 5)) for i in range(1, 10)]

    # Start Threads
    for t in threads:
        t.start()

    # Join Threads
    for t in threads:
        t.join()

    print("End")
    print("--- %s seconds ---" % (time.time() - start_time))


# ====================================
# Main Execution
# ====================================
if __name__ == "__main__":
    main()
