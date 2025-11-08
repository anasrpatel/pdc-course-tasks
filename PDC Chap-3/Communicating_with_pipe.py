import multiprocessing
from random import uniform
from time import sleep

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
# First Process: Create Items
# -----------------------------------------
def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        # simulate small delay
        sleep(0.5)
        print(f"Producing item: {item}")
        output_pipe.send(item)
    output_pipe.close()


# -----------------------------------------
# Second Process: Multiply Items + Weather
# -----------------------------------------
def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2

    try:
        while True:
            item = input_pipe.recv()
            result = item * item

            # Weather data simulation with each multiplication
            weather_total = weather_data_simulation()

            print(f"Processing item {item} → square={result:.2f} | Weather total={weather_total:.2f}")
            output_pipe.send((item, result, weather_total))
            sleep(0.5)
    except EOFError:
        output_pipe.close()


# -----------------------------------------
# Main Process
# -----------------------------------------
if __name__ == '__main__':
    print("\n=== Starting Pipe Communication with Weather Simulation ===\n")

    # First pipe (Producer)
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=create_items, args=(pipe_1,))
    process_pipe_1.start()

    # Second pipe (Processor)
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    # Close unused pipe ends in main process
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            item, squared, weather = pipe_2[1].recv()
            print(f"✅ Received from pipe → Item={item}, Square={squared}, Weather Total={weather:.2f}\n")
    except EOFError:
        print("\n--- End of Data Transmission ---")

    print("\n=== Program Completed ===")
