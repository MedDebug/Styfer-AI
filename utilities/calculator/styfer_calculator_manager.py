import math 
import cmath

def basic_calculation():                                   
    try:
        expression = input("Enter calculation: ")
        answer = eval(expression)                           #REPLACE EVAL IN THE FUTURE WITH SAFE MATH PARSER
        print(answer)                
    except Exception:
        print("Invalid expression.")
         
def squaring():
    try:
        num = float(input("Please enter the number: "))
        print(num**2)
    except ValueError:
        print("Please enter a valid number")
    
def square_root():
    try:
        num = float(input("Please enter the number: "))
        print(math.sqrt(num))
    except ValueError:
        print("Please enter a real non-negative number")
        
def cubing():
    try:
        num = float(input("Please enter the number: "))
        print(num**3)
    except ValueError:
        print("Please enter a valid number")
        
def cube_root():
    try:
        num = float(input("Please enter a valid number: "))
        print(math.cbrt(num))
    except ValueError:
        print("Please enter a real number")
        
def power():
    try:
        num = float(input("Please enter the number: "))
        magnitude = float(input("Please enter the magnitude"))
        print(num**magnitude)
    except ValueError:
        print("Please enter a valid number")

def quadratic_equations():
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    c = float(input("Enter value of c: "))
    discriminant = b*b - 4*a*c 
    if a == 0:
        print("This is not a quadratic equation")
        return
    if discriminant > 0:
        root = math.sqrt(discriminant)
        formula_1 = (- b - root)/(2*a) 
        formula_2 = (- b + root)/(2*a) 
        print("Roots are real and differ")
        print("1st Solution is: ", formula_1)
        print("2nd Solution is: ", formula_2)
    elif discriminant == 0:
        print("Roots are real and equal")
        print("Solution:",(-b/(2*a)))
    elif discriminant < 0:
        root = cmath.sqrt(discriminant)
        formula_1 = (- b - root)/(2*a) 
        formula_2 = (- b + root)/(2*a) 
        print("Roots are imaginary")
        print("1st solution is: ", formula_1)
        print("2nd solution is: ", formula_2)
        
def distance_formula():
    try:
        x_1 = float(input("Enter 1st X-axis coordinate: "))
        y_1 = float(input("Enter 1st Y-axis coordinate: "))
        x_2 = float(input("Enter 2nd X-axis coordinate: "))
        y_2 = float(input("Enter 2nd Y-axis coordinate: "))
        var = (x_2 - x_1)**2 + (y_2 - y_1)**2 
        formula = math.sqrt(var)
        print(formula)
    except ValueError:
        print("Please enter real numbers")