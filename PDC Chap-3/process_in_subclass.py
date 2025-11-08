import multiprocessing
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



class MyProcess(multiprocessing.Process):

    def run(self):
        print('called run method in %s' % self.name)
        return


if __name__ == '__main__':
    # Run weather simulation once
    total_value = weather_data_simulation()
    print("Simulated Weather Data Total:", total_value)

    # Run MyProcess class example (as it is)
    for i in range(10):
        process = MyProcess()
        process.start()
        process.join()
