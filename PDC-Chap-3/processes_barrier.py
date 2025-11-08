import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
from random import uniform


# ==================================
# Weather Data Simulation Function
# ==================================
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


# ==================================
# Barrier and Lock Multiprocessing 
# ==================================
def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s" %
              (name, datetime.fromtimestamp(now)))


def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" %
          (name, datetime.fromtimestamp(now)))


if __name__ == '__main__':
    # Run Weather Simulation once
    total_value = weather_data_simulation()
    print("\nSimulated Weather Data Total:", total_value, "\n")

    
    synchronizer = Barrier(2)
    serializer = Lock()

    Process(name='p1 - test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()

    Process(name='p2 - test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()

    Process(name='p3 - test_without_barrier',
            target=test_without_barrier).start()

    Process(name='p4 - test_without_barrier',
            target=test_without_barrier).start()
