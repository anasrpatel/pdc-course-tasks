import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Semaphore and shared data
semaphore = threading.Semaphore(0)
weather_data = None


# ==============================
# Weather Data Generation
# ==============================
def weather_calculations():
    temperature = round(random.uniform(20, 40), 2)
    humidity = random.randint(40, 90)
    wind_speed = round(random.uniform(5, 25), 2)
    pressure = round(random.uniform(990, 1030), 2)

    total = temperature + humidity + wind_speed + pressure
    return temperature, humidity, wind_speed, pressure, total


# ==============================
# Producer and Consumer
# ==============================
def consumer():
    global weather_data
    logging.info('Consumer is waiting for weather data...')
    semaphore.acquire()
    temp, hum, wind, pres, total = weather_data
    logging.info(
        f'Consumer received -> Temp={temp}°C, Humidity={hum}%, Wind={wind}km/h, Pressure={pres}hPa | Total={total:.2f}'
    )


def producer():
    global weather_data
    time.sleep(3)
    weather_data = weather_calculations()
    temp, hum, wind, pres, total = weather_data
    logging.info(
        f'Producer generated -> Temp={temp}°C, Humidity={hum}%, Wind={wind}km/h, Pressure={pres}hPa | Total={total:.2f}'
    )
    semaphore.release()


# ==============================
# Main Function
# ==============================
def main():
    for _ in range(10):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
