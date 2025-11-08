import multiprocessing
import time
from random import uniform

# -----------------------------------------
# Weather Data Simulation Function
# -----------------------------------------
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


# -----------------------------------------
# Function for Process (Original foo + Weather Simulation)
# -----------------------------------------
def foo():
    print('Starting function')
    for i in range(0, 10):
        weather_total = weather_data_simulation()
        print(f'--> {i} | Weather Total = {weather_total:.2f}\n')
        time.sleep(1)
    print('Finished function')


# -----------------------------------------
# Main Program (Original Killing Process Code)
# -----------------------------------------
if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())
    
    p.start()
    print('Process running:', p, p.is_alive())
    
    # Terminate process (as in original code)
    p.terminate()
    print('Process terminated:', p, p.is_alive())
    
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
