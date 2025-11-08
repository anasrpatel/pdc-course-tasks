import math
import logging
import threading
import time
from random import uniform

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

weather_data = []
condition = threading.Condition()


# ==============================
# Weather Calculations
# ==============================
def weather_calculations():
    temperature = uniform(20, 40)   # °C
    humidity = uniform(30, 90)      # %
    wind_speed = uniform(5, 25)     # km/h
    pressure = uniform(950, 1050)   # hPa

    heat_index = temperature + 0.33 * humidity - 0.7 * wind_speed - 4
    dew_point = temperature - ((100 - humidity) / 5)
    comfort_level = (100 - abs(temperature - 25)) + (humidity / 2) - (wind_speed / 3)
    total = heat_index + dew_point + comfort_level + pressure

    return total


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        with condition:
            if len(weather_data) == 0:
                logging.info('no weather data to consume')
                condition.wait()

            weather_data.pop()
            result = weather_calculations()   # <-- Weather function executes here
            logging.info(f'consumed 1 weather reading | calculation result: {result:.2f}')

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(2)
            self.consume()


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):
        with condition:
            if len(weather_data) == 10:
                logging.info('weather readings produced {}. Stopped'.format(len(weather_data)))
                condition.wait()

            weather_data.append(1)
            logging.info('total weather readings {}'.format(len(weather_data)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.produce()


def main():
    producer = Producer(name='Producer)')
    consumer = Consumer(name='Consumer)')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
