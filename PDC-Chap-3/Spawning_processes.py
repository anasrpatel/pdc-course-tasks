import multiprocessing
from random import uniform

# ================================
# Weather Simulation Function
# ================================
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


# ================================
# Multiprocessing Function
# ================================
def myFunc(i):
    print(f'Calling myFunc from process n°: {i}')
    for j in range(0, i):
        print(f'Output from myFunc is: {j}')
    # Call weather simulation for each process
    weather_value = weather_data_simulation()
    print(f'Weather simulation result from process {i}: {weather_value:.2f}\n')
    return


# ================================
# Main Program
# ================================
if __name__ == '__main__':
    print("=== Weather Simulation with Multiprocessing ===\n")
    processes = []

    # Spawn multiple processes
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("\nAll weather simulations completed successfully!")
