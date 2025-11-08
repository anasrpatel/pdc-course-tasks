import math
import time
import os
import random
from threading import Thread

# -------------------------------------
# Weather Calculations Function
# -------------------------------------
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


# -------------------------------------
# Thread Class
# -------------------------------------
class MyThreadClass(Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name

   def run(self):
      print(f"--> {self.name} running in Process ID: {os.getpid()}")
      result = weather_calculations()
      print(f"--> {self.name} Weather Result = {result:.2f}\n")


# -------------------------------------
# Main Function
# -------------------------------------
def main():
    start_time = time.time()

    # Creating Threads
    threads = []
    for i in range(1, 10):
        threads.append(MyThreadClass(f"Thread#{i}"))

    # Start Threads
    for t in threads:
        t.start()

    # Join Threads
    for t in threads:
        t.join()

    print("End")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
