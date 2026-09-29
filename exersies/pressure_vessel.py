#values
internal_pressure = float(input("enter pressure in bar: "))
wall_temp =float(input("enter wall temperature in Celsius: "))
vessel_vibration = float(input("enter vessel vibration in mm/s: "))

#deliberations
pressure_safe = 5 <= internal_pressure <= 15
temperature_safe = 20 <= wall_temp <= 250
vibration_safe =  vessel_vibration < 4

#outputs
if pressure_safe and temperature_safe and vibration_safe:
    print("The pressure vessel is safe to operate.")
elif temperature_safe and vibration_safe and not pressure_safe:
    print("The pressure vessel is unsafe to operate due to pressure.")
elif pressure_safe and vibration_safe and not temperature_safe:
    print("The pressure vessel is unsafe to operate due to temperature.")
elif pressure_safe and temperature_safe and not vibration_safe:
    print("The pressure vessel is unsafe to operate due to vibration.") 
else:
    print("The pressure vessel is unsafe to operate due to multiple factors.")