import multiprocessing
import random
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
# Producer Process (Generate Items + Weather)
# -----------------------------------------
class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)

            # Call weather simulation for each item
            weather_total = weather_data_simulation()

            # Put both item + weather info into queue
            self.queue.put((item, weather_total))

            print(f"🌦️ Producer: Item={item} | Weather Total={weather_total:.2f} | Added by {self.name}")
            time.sleep(1)

            print(f"📦 Queue size is now {self.queue.qsize()}\n")

        print("✅ Producer finished adding all items!\n")


# -----------------------------------------
# Consumer Process (Consume Items + Weather)
# -----------------------------------------
class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("⚠️ Queue is empty, consumer stopping...\n")
                break
            else:
                time.sleep(2)
                item, weather_total = self.queue.get()
                print(f"🧾 Consumer: Got item={item} | Weather Total={weather_total:.2f} | From {self.name}\n")
                time.sleep(1)


# -----------------------------------------
# Main Section
# -----------------------------------------
if __name__ == '__main__':
    print("\n=== Communicating with Queue + Weather Simulation ===\n")

    queue = multiprocessing.Queue()

    process_producer = Producer(queue)
    process_consumer = Consumer(queue)

    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()

    print("🏁 Program Finished Successfully!\n")
