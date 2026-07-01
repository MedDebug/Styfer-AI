import math
from voice_hub import ask,speak,say,get_float,get_int,get_non_zero_float
    
#---------------------------------------------------------------------

def speed_distance_time():
    print("------Speed / Distance / Time------------")
    print()
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "speed":
        get_distance = get_float("Enter distance: ")
        get_time = get_non_zero_float("Enter time: ", "Time")
        say(f"Resultant: {get_distance/get_time}")
            
    elif answer == "distance":
        get_speed = get_float("Enter speed: ")
        get_time = get_float("Enter time: ",)
        say(f"Result: {get_speed*get_time}")
    
    elif answer == "time":
        get_distance = get_float("Enter distance: ")
        get_speed = get_non_zero_float("Enter speed: ", "Speed")
        say(f"Result: {get_distance/get_speed}")
    else:
        say("Please enter a valid field from the above")
        
def velocity_displacement_time():
    print("------Velocity / Displacement / Time------------")
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "velocity":
        get_displacement = get_float("Enter displacement: ")
        get_time = get_non_zero_float("Enter time: ", "Time")
        say(f"Result: {get_displacement/get_time}")
        
    elif answer == "displacement":
        get_velocity = get_float("Enter velocity: ")
        get_time = get_float("Enter time: ")
        say(f"Result: {get_velocity*get_time}")
    
    elif answer == "time":
        get_displacement = get_float("Enter displacement: ")
        get_velocity = get_non_zero_float("Enter velocity: ", "Velocity")
        say(f"Result: {get_displacement/get_velocity}")
    else:
        say("Please enter a valid field from the above")
        
def acceleration_velocity_time():
    print("------Acceleration / Velocity / Time------------")
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "acceleration":
        get_velocity = get_float("Enter velocity: ")
        get_time = get_non_zero_float("Enter time: ", "Time") 
        say(f"Result: {get_velocity/get_time}")
        
    elif answer == "velocity":
        get_acceleration = get_float("Enter acceleration: ")
        get_time = get_float("Enter time: ")
        say(f"Result: {get_acceleration*get_time}")
    
    elif answer == "time":       
        get_acceleration = get_non_zero_float("Enter acceleration: ", "Acceleration")
        get_velocity = get_float("Enter velocity: ")
        say(f"Result: {get_velocity/get_acceleration}")
    else:
        say("Please enter a valid field from the above")
        
def force_mass_acceleration():
    print("------Force / Mass / Acceleration------------")
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "acceleration":
        get_force = get_float("Enter force: ")
        get_mass = get_non_zero_float("Enter mass: ", "Mass") 
        say(f"Result: {get_force/get_mass}")
        
    elif answer == "force":
        get_acceleration = get_float("Enter acceleration: ")
        get_mass = get_non_zero_float("Enter mass: ", "Mass")
        say(f"Result: {get_acceleration*get_mass}")
    
    elif answer == "mass":       
        get_acceleration = get_non_zero_float("Enter acceleration: ", "Acceleration")
        get_force = get_float("Enter force: ")
        say(f"Result: {get_force/get_acceleration}")
    else:
        say("Please enter a valid field from the above")
        
def momentum_mass_velocity():
    print("------Momentum / Mass / Velocity------------")
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "velocity":
        get_momentum = get_float("Enter momentum: ")
        get_mass = get_non_zero_float("Enter mass: ", "Mass") 
        say(f"Result: {get_momentum/get_mass}")
        
    elif answer == "momentum":
        get_velocity = get_float("Enter velocity: ")
        get_mass = get_non_zero_float("Enter mass: ", "Mass")
        say(f"Result: {get_velocity*get_mass}")
    
    elif answer == "mass":       
        get_velocity = get_non_zero_float("Enter velocity: ", "Velocity")
        get_momentum = get_float("Enter momentum: ")
        say(f"Result: {get_momentum/get_velocity}")
    else:
        say("Please enter a valid field from the above")
        
def impulse_force_time():
    print("------Impulse / Force / Time------------")
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "force":
        get_impulse = get_float("Enter impulse: ")
        get_time = get_non_zero_float("Enter time: ", "Time") 
        say(f"Result: {get_impulse/get_time}")
        
    elif answer == "impulse":
        get_force = get_float("Enter force: ")
        get_time = get_non_zero_float("Enter time: ", "Time")
        say(f"Result: {get_force*get_time}")
    
    elif answer == "time":       
        get_force = get_non_zero_float("Enter force: ", "Force")
        get_impulse = get_float("Enter impulse: ")
        say(f"Result: {get_impulse/get_force}")
    else:
        say("Please enter a valid field from the above")
        
def torque_force_radius():
    print("------Torque / Force / Radius------------")
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "force":
        get_torque = get_float("Enter torque: ")
        get_radius = get_non_zero_float("Enter radius: ", "Radius") 
        say(f"Result: {get_torque/get_radius}")
        
    elif answer == "torque":
        get_force = get_float("Enter force: ")
        get_radius = get_non_zero_float("Enter radius: ", "Radius")
        say(f"Result: {get_force*get_radius}")
    
    elif answer == "radius":       
        get_force = get_non_zero_float("Enter force: ", "Force")
        get_torque = get_float("Enter torque: ")
        say(f"Result: {get_torque/get_force}")
    else:
        say("Please enter a valid field from the above")
        
def work_force_displacement():
    print("------Work / Force / Displacement------------")
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "force":
        get_work = get_float("Enter work: ")
        get_displacement = get_non_zero_float("Enter displacement: ", "Displacement") 
        say(f"Result: {get_work/get_displacement}")
        
    elif answer == "work":
        get_force = get_float("Enter force: ")
        get_displacement = get_non_zero_float("Enter displacement: ", "Displacement")
        say(f"Result: {get_force*get_displacement}")
    
    elif answer == "displacement":       
        get_force = get_non_zero_float("Enter force: ", "Force")
        get_work = get_float("Enter work: ")
        say(f"Result: {get_work/get_force}")
    else:
        say("Please enter a valid field from the above")
        
def potential_mass_height():
    print("------Potential Energy / Mass / Height------------")
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "height":
        get_potential = get_float("Enter potential energy: ")
        get_mass = get_non_zero_float("Enter mass: ", "Mass") 
        say(f"Result: {get_potential/(get_mass*9.8)}")
        
    elif answer == "potential":
        get_height = get_float("Enter height: ")
        get_mass = get_non_zero_float("Enter mass: ", "Mass")
        say(f"Result: {get_height*get_mass*9.8}")
    
    elif answer == "mass":       
        get_height = get_non_zero_float("Enter height: ", "Height")
        get_potential = get_float("Enter potential energy: ")
        say(f"Result: {get_potential/(get_height*9.8)}")
    else:
        say("Please enter a valid field from the above")
        
def kinetic_mass_velocity():
    print("------Kinetic Energy / Mass / Velocity------------")
    answer = ask("Enter the field which you would like to calculate: ").lower()
    if answer == "velocity":
        get_kinetic = get_float("Enter kinetic energy: ")
        get_mass = get_non_zero_float("Enter mass: ", "Mass") 
        say(f"Result: {math.sqrt((2*get_kinetic)/get_mass)}")
        
    elif answer == "kinetic":
        get_velocity = get_float("Enter velocity: ")
        get_mass = get_non_zero_float("Enter mass: ", "Mass")
        say(f"Result: {(get_mass*(get_velocity**2))/2}")
    
    elif answer == "mass":       
        get_velocity = get_non_zero_float("Enter velocity: ", "Velocity")
        get_kinetic = get_float("Enter kinetic energy: ")
        say(f"Result: {(2*get_kinetic)/(get_velocity**2)}")
    else:
        say("Please enter a valid field from the above")