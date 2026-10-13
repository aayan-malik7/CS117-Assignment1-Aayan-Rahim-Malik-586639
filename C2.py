#Parallel Resistance 

#Formula: 1 / R_eq = 1/R1 + 1/R2 + ...

def parallel_resistance(resistors):   #Defining a function to calculate the equivalent resistance in parallel
    reciprocal_sum = 0                # Initialization for the sum of reciprocals 
    
    for r in resistors:
        reciprocal_sum = reciprocal_sum + 1 / r          # Add the reciprocal of the resistor
    return round(1 / reciprocal_sum, 2)


print("parallel_resistance([5, 5]) ->", parallel_resistance([5, 5]))    #Testing the function with a pair of 5 ohm resistors, answer should be 2.5 ohm

print("parallel_resistance([100, 200, 300]) ->", parallel_resistance([100, 200, 300]))      #Testing the function with three different resistors