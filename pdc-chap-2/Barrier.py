import math
from random import randrange, uniform
from threading import Barrier, Thread
from time import ctime, sleep

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
# Thread Race Code With Weather Simulation
# -----------------------------------------
num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner(name):
    sleep(randrange(2, 5))
    print(f'{name} reached the barrier at: {ctime()}')
    
    # Call Weather Data Simulation
    result = weather_data_simulation()
    print(f'{name} calculated weather total = {result:.2f}\n')
    
    finish_line.wait()

def main():
    threads = []
    print('START RACE!!!!\n')
    
    for name in runners:
        t = Thread(target=runner, args=(name,))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()
    
    print('\nRace over!')

if __name__ == "__main__":
    main()
