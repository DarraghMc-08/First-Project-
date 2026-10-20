#engine info 
line = "engine 1; 1200 rpm; 85 C; 30 l"

#split into parts 
parts = line.split(";")

#configure each part  
name = parts[0].strip()
rpm = int(parts[1].strip().split(" rpm")[0])
temp = int(parts[2].strip().split(" C")[0])
fuel = int(parts[3].strip().split(" l")[0])
#print info
print(f"Engine Name: {name}")
print(f"RPM: {rpm} RPM")
print(f"Temperature: {temp} C")
print(f"Fuel: {fuel} l")


