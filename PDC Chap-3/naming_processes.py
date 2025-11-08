import multiprocessing
import time
from random import uniform

# ==============================
# Weather Data Simulation
# ==============================
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


# ==============================
# myFunc Process Example (as it is)
# ==============================
def myFunc():
    name = multiprocessing.current_process().name
    print("Starting process name = %s \n" % name)
    time.sleep(3)
    print("Exiting process name = %s \n" % name)


if __name__ == '__main__':
    # Run weather simulation
    print("Simulated Weather Data Total:", weather_data_simulation())

    # Run multiprocessing example (as given)
    process_with_name = multiprocessing.Process(
        name='myFunc process',
        target=myFunc
    )

    #process_with_name.daemon = True

    process_with_default_name = multiprocessing.Process(
        target=myFunc
    )

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()
