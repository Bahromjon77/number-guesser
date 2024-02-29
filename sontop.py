import random

n= random.randint(0,10)

guesst = int(input("0 va 10 orasidagi ihtiyoriy sonni kiriting:"))

if n == guesst:
    print("Topdingiz")
else:
    print("Topaolmadingiz")
