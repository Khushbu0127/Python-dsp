# Practical 5: User-defined + Built-in module

# --- Part A: User-defined module (khud ke function) ---
def add(a,b):
    return a+b

def mul(a,b):
    return a*b

PI = 3.14

# --- Part B: Built-in module ka use ---
import math

print("--- User-defined module se ---")
print("Addition:", add(10, 20))
print("Multiplication:", mul(5, 4))
print("PI value:", PI)

print("\n--- Built-in math module se ---")
print("Square root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Power 2^3:", math.pow(2,3))
print("Value of pi:", math.pi)
