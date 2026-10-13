# Finding the total resistance

num_of_resistors = int(input("How many resistors: "))                    #taking input from user for number of resistors

total_resistance = 0                                          #taking reference of total resistance as 0

for i in range(1, num_of_resistors + 1):
    resistance = float(input("Enter R" + str(i) + ": "))       #str(i): Converts the number i into text so it can be combined with "Enter R", which is text
    total_resistance = total_resistance + resistance

print("Total resistance =", total_resistance, "ohm")