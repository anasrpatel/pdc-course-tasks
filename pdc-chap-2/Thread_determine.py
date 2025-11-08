import threading
import time
from random import uniform

# ============================
# Weather Simulation Function
# ============================
def weather_data_simulation():
    # Random weather parameters
    temperature = uniform(20, 40)   # °C
    humidity = uniform(30, 90)      # %
    wind_speed = uniform(5, 25)     # km/h
    pressure = uniform(950, 1050)   # hPa

    # Basic weather calculations
    heat_index = temperature + 0.33 * humidity - 0.7 * wind_speed - 4
    dew_point = temperature - ((100 - humidity) / 5)
    comfort_level = (100 - abs(temperature - 25)) + (humidity / 2) - (wind_speed / 3)

    total = heat_index + dew_point + comfort_level + pressure

    # Return all results
    return {
        "Temperature": temperature,
        "Humidity": humidity,
        "Wind Speed": wind_speed,
        "Pressure": pressure,
        "Total": total
    }

# ============================
# Thread Functions
# ============================
def function_A():
    print(threading.currentThread().getName() + " --> starting\n")
    time.sleep(2)
    result = weather_data_simulation()
    print(threading.currentThread().getName() + f" --> Weather Data:\n"
          f"   Temperature: {result['Temperature']:.2f}°C\n"
          f"   Humidity: {result['Humidity']:.2f}%\n"
          f"   Wind Speed: {result['Wind Speed']:.2f} km/h\n"
          f"   Pressure: {result['Pressure']:.2f} hPa\n"
          f"   Total: {result['Total']:.2f}\n")
    print(threading.currentThread().getName() + " --> exiting\n")

def function_B():
    print(threading.currentThread().getName() + " --> starting\n")
    time.sleep(2)
    result = weather_data_simulation()
    print(threading.currentThread().getName() + f" --> Weather Data:\n"
          f"   Temperature: {result['Temperature']:.2f}°C\n"
          f"   Humidity: {result['Humidity']:.2f}%\n"
          f"   Wind Speed: {result['Wind Speed']:.2f} km/h\n"
          f"   Pressure: {result['Pressure']:.2f} hPa\n"
          f"   Total: {result['Total']:.2f}\n")
    print(threading.currentThread().getName() + " --> exiting\n")

def function_C():
    print(threading.currentThread().getName() + " --> starting\n")
    time.sleep(2)
    result = weather_data_simulation()
    print(threading.currentThread().getName() + f" --> Weather Data:\n"
          f"   Temperature: {result['Temperature']:.2f}°C\n"
          f"   Humidity: {result['Humidity']:.2f}%\n"
          f"   Wind Speed: {result['Wind Speed']:.2f} km/h\n"
          f"   Pressure: {result['Pressure']:.2f} hPa\n"
          f"   Total: {result['Total']:.2f}\n")
    print(threading.currentThread().getName() + " --> exiting\n")

# ============================
# Main
# ============================
if __name__ == "__main__":
    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("✅ All weather threads completed successfully.")
