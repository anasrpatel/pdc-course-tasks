import threading
import random

# =====================================
# Function: Weather Calculations
# =====================================
def weather_calculations():
    temperature = round(random.uniform(20, 40), 2)
    humidity = random.randint(40, 90)
    wind_speed = round(random.uniform(5, 25), 2)
    pressure = round(random.uniform(990, 1030), 2)

    total = temperature + humidity + wind_speed + pressure
    return total


# =====================================
# Thread Function
# =====================================
def my_func(thread_number):
    result = weather_calculations()
    print(f"Thread {thread_number} | Weather Total = {result:.2f}")


# =====================================
# Main Program
# =====================================
def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()  # waits for thread to finish before starting next one


if __name__ == "__main__":
    main()
