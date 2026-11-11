
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

class WeatherAnalysis:
    def __init__(self, date_str, time_str, temperature, humidity, pressure):
        self.date_str = datetime.strptime(date_str, "%Y-%m-%d")
        self.time_str = datetime.strptime(time_str, "%H:%M")
        self.temperature = float(temperature)
        self.humidity = float(humidity)
        self.pressure = float(pressure)

data = []

with open("exersies/weather_data.csv") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        try: 
            fields = line.split(",")
            r = WeatherAnalysis(*fields)
            data.append(r) 
        except (ValueError, IndexError) as e:
            print(f"Error processing line: {line}. Error: {e}")

print(f"Loaded {len(data)} records.")

specific_date = datetime.strptime(input("Enter date to filter (YYYY-MM-DD): "), "%Y-%m-%d").date()
temps_for_date = {
    r.temperature for r in data
    if r.date_str.date() == specific_date
}
avg_temp = np.mean(list(temps_for_date)) if temps_for_date else None
print(f"Temperatures on {specific_date}: {temps_for_date}")
if avg_temp is not None:
    print(f"Average temperature on {specific_date}: {avg_temp:.2f} C")

temps= np.array([r.temperature for r in data])
print(f"avg {temps.mean():.2f} C, max {temps.max():.2f} C, min {temps.min():.2f} C")
