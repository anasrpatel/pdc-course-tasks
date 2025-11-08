from threading import Thread
from random import uniform
import time

# =================================
# Function: Weather Data Simulation
# =================================
def weather_data_simulation():
    temperature = uniform(20, 40)   # °C
    humidity = uniform(30, 90)      # %
    wind_speed = uniform(5, 25)     # km/h
    pressure = uniform(950, 1050)   # hPa

    # Weather-based calculations
    heat_index = temperature + 0.33 * humidity - 0.7 * wind_speed - 4
    dew_point = temperature - ((100 - humidity) / 5)
    comfort_level = (100 - abs(temperature - 25)) + (humidity / 2) - (wind_speed / 3)

    total = heat_index + dew_point + comfort_level + pressure
    return total


# =================================
# Thread Class
# =================================
class MyThreadClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        result = weather_data_simulation()
        print(f"{self.name} → Weather Total = {result:.2f}")


# =================================
# Main Function
# =================================
def main():
    # Creating threads
    thread1 = MyThreadClass("Thread #1")
    thread2 = MyThreadClass("Thread #2")

    # Starting threads
    thread1.start()
    thread2.start()

    # Waiting for threads to complete
    thread1.join()
    thread2.join()

    print("End")


# =================================
# Run Program
# =================================
if __name__ == "__main__":
    main()
