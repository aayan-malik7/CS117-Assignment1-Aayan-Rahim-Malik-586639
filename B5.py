#Resistor Tolerance Sorting

# Initializing counters 
one_percent = 0
five_percent = 0
rejected = 0


# Getting the initial measured resistance value from the user
measured = float(input("Enter measured resistance: "))

while measured != 0:                                #run the loop until the user enters 0
    if 99.0 <= measured <= 101.0:                   #Check if the measured value is between 99.0 to 101.0 ohms
        one_percent = one_percent + 1

    elif 95.0 <= measured <= 105.0:                 #Check if the written value is between 95.0 to 105.0 ohms
     five_percent = five_percent + 1
        
    else:                                           #If it doesn't meet either tolerance, 
        rejected = rejected + 1                     
    measured = float(input("Enter measured resistance (0 to stop): "))


print("1% tolerance:", one_percent)
print("5% tolerance:", five_percent)
print("Reject:", rejected)