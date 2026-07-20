import math
import random
import platform

randomN = random.randint(1, 100)

print("Random Number: ", randomN)

Sroot = math.sqrt(randomN)
print("Squre Root: ", math.floor(Sroot))

print("OS: ", platform.system())
print("Python version: ", platform.python_implementation())