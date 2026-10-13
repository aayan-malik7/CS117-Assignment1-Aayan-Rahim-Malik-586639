#Finding the smallest and largest of 3 resistors 

r1 = float(input("Enter R1: "))
r2 = float(input("Enter R2: "))
r3 = float(input("Enter R3: "))

#we will use AND here because AND returns True only if both conditions are True
if r1 <= r2 and r1 <= r3:
    smallest = r1
elif r2 <= r1 and r2 <= r3:
    smallest = r2
else:
    smallest = r3
#again using AND here to check the largest resistor
if r1 >= r2 and r1 >= r3:
    largest = r1
elif r2 >= r1 and r2 >= r3:
    largest = r2
else:
    largest = r3

print("Smallest =", smallest, "ohm")
print("Largest =", largest, "ohm")