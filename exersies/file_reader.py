import csv
from pathlib import Path


input_file = Path(__file__).with_name("datafile.csv")
output_file = "voltages_normalised.csv"

readings = []
with open(input_file, newline="", encoding="utf-8-sig") as file:
	for row in csv.reader(file):
		if len(row) < 2:
			continue
		try:
			readings.append((float(row[0]), row[1]))
		except ValueError:
			# Ignore a non-numeric header row.
			continue

if not readings:
	raise ValueError(f"No (voltage, time) readings found in {input_file}")

voltages = [voltage for voltage, _ in readings]
v_ave = sum(voltages) / len(voltages)
print(f"V_ave = {v_ave}")

max_voltage = max(voltages)
with open(output_file, "w", newline="", encoding="utf-8") as file:
	writer = csv.writer(file)
	writer.writerow(["Normalised voltage", "Time"])
	writer.writerows([voltage / max_voltage, time] for voltage, time in readings)
