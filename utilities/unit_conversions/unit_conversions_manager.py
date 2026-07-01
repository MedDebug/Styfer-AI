from voice_hub import ask,say,speak,get_float,get_int,get_non_zero_float

volume = {"m3": 1,
          "dm3": 0.001,
          "cm3": 0.000001,
          "litres": 0.001,
          "millilitres": 0.000001}
def volume_conversions():
    while True:
        print("------- dm3 / cm3 / m3 / Litres / Millilitres--------")
        
        unknown_field = ask("Please enter one field from the above: ").lower()
        known_field = ask("Please enter the field of the value which you currently have: ").lower()
        
        if known_field not in volume or unknown_field not in volume:
            say("Please enter a valid unit.")
            continue
        
        known_value = get_float("Please enter the value of that field: ")
        base_value = known_value*volume[known_field]
        answer = base_value / volume[unknown_field]
        say(f"Resultant: {answer}")
        break

area = {
    "mm2": 0.000001,
    "cm2": 0.0001,
    "dm2": 0.01,
    "m2": 1,
    "km2": 1000000,
    "hectares": 10000,
    "acres": 4046.8564224
}
def area_conversions():
    while True:
        print("------- mm2 / cm2 / m2 / dm2 / km2 / Hectares / Acres--------")
        unknown_field = ask("Please enter one field from the above").lower()
        known_field = ask("Please enter the field of the value which you currently have: ").lower()
        
        if known_field not in area or unknown_field not in area:
            say("Please enter a valid unit.")
            continue
        
        known_value = get_float("Please enter the value of that field: ")
        base_value = known_value*area[known_field]
        answer = base_value / area[unknown_field]
        say(f"Resultant: {answer}")
        break

length = {
    "mm": 0.001,
    "cm": 0.01,
    "dm": 0.1,
    "m": 1,
    "km": 1000,
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.9144,
    "miles": 1609.344
}
def length_distance_conversions():
    while True:
        print("------- mm / cm / m / dm / km / Inches / Feet / Yards / Miles--------")
        unknown_field = ask("Please enter one field from the above").lower()
        known_field = ask("Please enter the field of the value which you currently have: ").lower()
        
        if known_field not in length or unknown_field not in length:
            say("Please enter a valid unit.")
            continue
        
        known_value = get_float("Please enter the value of that field: ")
        base_value = known_value*length[known_field]
        answer = base_value / length[unknown_field]
        say(f"Resultant: {answer}")
        break
    
mass = {
    "mg": 0.000001,
    "g": 0.001,
    "kg": 1,
    "tonnes": 1000,
    "ounces": 0.0283495,
    "pounds": 0.45359237
}
def mass_conversions():
    while True:
        print("----------mg / g / kg / Tonnes / Ounces / Pounds----------")
        unknown_field = ask("Please enter one field from the above").lower()
        known_field = ask("Please enter the field of the value which you currently have: ").lower()
        
        if known_field not in mass or unknown_field not in mass:
            say("Please enter a valid unit.")
            continue
        
        known_value = get_float("Please enter the value of that field: ")
        base_value = known_value*mass[known_field]
        answer = base_value / mass[unknown_field]
        say(f"Resultant: {answer}")
        break
        
time = {
    "milliseconds": 0.001,
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
    "days": 86400,
    "weeks": 604800
}
def time_conversions():
    while True:
        print("----------Milliseconds / Seconds / Minutes / Hours / Days / Weeks----------")
        unknown_field = ask("Please enter one field from the above").lower()
        known_field = ask("Please enter the field of the value which you currently have: ").lower()
        
        if known_field not in time or unknown_field not in time:
            say("Please enter a valid unit.")
            continue
        
        known_value = get_float("Please enter the value of that field: ")
        base_value = known_value*time[known_field]
        answer = base_value / time[unknown_field]
        say(f"Resultant: {answer}")
        break
    
def temperature_conversions():
    while True:
        print("----------Kelvin / Celsius / Fahrenheit----------")
        unknown_field = ask("Please enter one field from the above").lower()
        known_field = ask("Please enter the field of the value which you currently have: ").lower()
        valid = ["celsius", "fahrenheit", "kelvin"]
        if known_field not in valid or unknown_field not in valid:
            say("Please enter a valid unit.")
            continue
        known_value = get_float("Please enter the value of that field: ")
        if unknown_field == known_field:
            say(f"Resultant:  {known_value}")
            break
        
        elif unknown_field == "celsius":
            if known_field == "fahrenheit":
                say(f"Resultant: {(known_value-32)*(5/9)}")
                break
            elif known_field == "kelvin":
                say(f"Resultant: {known_value - 273.15}")
                break
        
        elif unknown_field == "fahrenheit":
            if known_field == "celsius":
                say(f"Resultant: {(known_value*(9/5)) + 32}")
                break
            elif known_field == "kelvin":
                say(f"Resultant: {(known_value - 273.15)*(9/5) + 32}")
                break
        
        elif unknown_field == "kelvin":
            if known_field == "celsius":
                say(f"Resultant: {known_value + 273.15}")
                break
            elif known_field == "fahrenheit":
                say(f"Resultant: {(known_value - 32)*(5/9) + 273.15}")
                break
        else:
            say("Please enter a valid field from the above")
            continue
        
speed = {
    "m/s": 1,
    "km/h": 0.2777777778,
    "mph": 0.44704,
    "ft/s": 0.3048,
    "knots": 0.514444
}
def speed_conversions():
    while True:
        print("----------m/s / km/h / mph / ft/s / knots----------")

        unknown_field = ask("Please enter one field from the above: ").lower()
        known_field = ask("Please enter the field of the value which you currently have: ").lower()

        if known_field not in speed or unknown_field not in speed:
            say("Please enter a valid unit.")
            continue

        known_value = get_float("Please enter the value of that field: ")
        base_value = known_value * speed[known_field]
        answer = base_value / speed[unknown_field]

        say(f"Resultant: {answer}")
        break
    
pressure = {
    "pascal": 1,
    "kpa": 1000,
    "mpa": 1000000,
    "bar": 100000,
    "atm": 101325,
    "psi": 6894.757,
    "torr": 133.322
}
def pressure_conversions():
    while True:
        print("----------Pascal / kpa / mpa / Bar / atm / psi / Torr----------")

        unknown_field = ask("Please enter one field from the above: ").lower()
        known_field = ask("Please enter the field of the value which you currently have: ").lower()

        if known_field not in pressure or unknown_field not in pressure:
            say("Please enter a valid unit.")
            continue

        known_value = get_float("Please enter the value of that field: ")
        base_value = known_value * pressure[known_field]
        answer = base_value / pressure[unknown_field]

        say(f"Resultant: {answer}")
        break
    
energy = {
    "joule": 1,
    "kj": 1000,
    "mj": 1000000,
    "cal": 4.184,
    "kcal": 4184,
    "wh": 3600,
    "kwh": 3600000,
    "ev": 1.602176634e-19
}
def energy_conversions():
    while True:
        print("----------Joule / kj / mj / cal / kcal / wh / kwh / ev----------")

        unknown_field = ask("Please enter one field from the above: ").lower()
        known_field = ask("Please enter the field of the value which you currently have: ").lower()

        if known_field not in energy or unknown_field not in energy:
            say("Please enter a valid unit.")
            continue

        known_value = get_float("Please enter the value of that field: ")
        base_value = known_value * energy[known_field]
        answer = base_value / energy[unknown_field]

        say(f"Resultant: {answer}")
        break
    