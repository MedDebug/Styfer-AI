import math 
import cmath
from voice_hub import ask,say,speak,get_float, get_int

def basic_calculation():                                   
    try:
        expression = ask("Enter calculation: ")
        answer = eval(expression)                           #REPLACE EVAL IN THE FUTURE WITH SAFE MATH PARSER
        say(f"Resultant: {answer}")                
    except Exception:
        say("Invalid expression.")
         
def squaring():
    num = get_float(("Please enter the number: "))
    say(f"Resultant: {num**2}")
    
def square_root():
    num = get_float("Please enter the number: ")
    if num < 0:
        say("Please enter a real non-negative number")
        return
    say(f"Resultant: {math.sqrt(num)}")
        
def cubing():
    num = get_float(("Please enter the number: "))
    say(f"Resultant: {num**3}")

        
def cube_root():
    num = get_float(("Please enter a valid number: "))
    say(f"Resultant: {math.cbrt(num)}")
        
def power():
    num = get_float(("Please enter the number: "))
    magnitude = get_float(("Please enter the magnitude: "))
    say(f"Resultant: {num**magnitude}")


def quadratic_equations():
    a = get_float(("Enter value of a: "))
    b = get_float(("Enter value of b: "))
    c = get_float(("Enter value of c: "))
    discriminant = b*b - 4*a*c 
    if a == 0:
        say("This is not a quadratic equation")
        return
    if discriminant > 0:
        root = math.sqrt(discriminant)
        formula_1 = (- b - root)/(2*a) 
        formula_2 = (- b + root)/(2*a) 
        say("Roots are real and different")
        say(f"1st Solution is:  {formula_1}")
        say(f"2nd Solution is: {formula_2}")
    elif discriminant == 0:
        say("Roots are real and equal")
        say(f"Solution: {(-b/(2*a))}")
    elif discriminant < 0:
        root = cmath.sqrt(discriminant)
        formula_1 = (- b - root)/(2*a) 
        formula_2 = (- b + root)/(2*a) 
        say("Roots are imaginary")
        say(f"1st solution is:  {formula_1}")
        say(f"2nd solution is: {formula_2}")
        
def distance_formula():
    x_1 = get_float(("Enter 1st X-axis coordinate: "))
    y_1 = get_float(("Enter 1st Y-axis coordinate: "))
    x_2 = get_float(("Enter 2nd X-axis coordinate: "))
    y_2 = get_float(("Enter 2nd Y-axis coordinate: "))
    var = (x_2 - x_1)**2 + (y_2 - y_1)**2 
    formula = math.sqrt(var)
    say(f"Resultant: {formula}")