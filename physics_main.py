from physics_manager import speed_distance_time, velocity_displacement_time, acceleration_velocity_time, force_mass_acceleration, momentum_mass_velocity, impulse_force_time, torque_force_radius, work_force_displacement, potential_mass_height, kinetic_mass_velocity 
from physics_menu import physics_menu

def run_physics_manager():
    while True:
        physics_menu()
        try:
            answer = int(input("Please enter an integer from 1 to 11 (inclusive): "))
        except ValueError:
            print("Please enter a valid integer from 1 to 11 (inclusive) ")
            continue
        
        if answer == 1:
            speed_distance_time()
        elif answer == 2:
            velocity_displacement_time()
        elif answer == 3:
            acceleration_velocity_time()
        elif answer == 4:
            force_mass_acceleration()
        elif answer == 5:
            momentum_mass_velocity()
        elif answer == 6:
            impulse_force_time()
        elif answer == 7:
            torque_force_radius()
        elif answer == 8:
            work_force_displacement()
        elif answer == 9:
            potential_mass_height()
        elif answer == 10:
            kinetic_mass_velocity()
        elif answer == 11:
            print("Thank you for using Styfer AI Physics Toolkit")
            break
        else:
            print("Please enter a valid integer from 1 to 11 (inclusive) ")