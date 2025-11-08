import multiprocessing
import time
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
# Background vs Non-Background Processes 
# ==================================
def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    if name == 'background_process':
        for i in range(0, 5):
            print('---> %d \n' % i)
        time.sleep(1)
    else:
        for i in range(5, 10):
            print('---> %d \n' % i)
        time.sleep(1)
    print("Exiting %s \n" % name)


if __name__ == '__main__':
    # Run Weather Simulation once
    total_value = weather_data_simulation()
    print("\nSimulated Weather Data Total:", total_value, "\n")

    # Run both processes (daemon=False for both)
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = False

    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()
