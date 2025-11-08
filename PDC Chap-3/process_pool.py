import multiprocessing
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
# Using a Process Pool 
# ==================================
def function_square(data):
    result = data * data
    return result


if __name__ == '__main__':
    # Run weather simulation once
    total_value = weather_data_simulation()
    print("Simulated Weather Data Total:", total_value)

    # Process Pool example (as it is)
    inputs = list(range(0, 100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)

    pool.close()
    pool.join()

    print('Pool :', pool_outputs)
