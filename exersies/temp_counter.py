# Temperature Counter
import random

temperatures = [random.randint(-10, 40) for _ in range(20)]

average_temperature = sum(temperatures) / len(temperatures)
below_zero = sum(temperature < 0 for temperature in temperatures)

print("Average temperature:", average_temperature, "C")
print("Number of temperatures below 0 C:", below_zero)
