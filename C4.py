#Voltage Divider

# Defining a function to calculate output voltage with and without a load resistor (rL)
def loaded_divider(vs, r1, r2, rl):         # Vs = supplied voltage, r1 = top resistor, r2 = bottom resistor, rl = load resistor

    #Calculating the ideal (without load) output voltage using the voltage divider formula
    unloaded = vs * r2 / (r1 + r2)

    #r2 and load are in parallel, so finding equivalent first
    r_parallel = (r2 * rl) / (rl + r2)              

    
    with_load = vs * r_parallel / (r_parallel+r1)        #calculating the loaded output voltage by putting the equivalent parallel resistance into the divider formula

    return round(unloaded, 2), round(with_load, 2)


print("loaded_divider(12, 1000, 1000, 500) ->", loaded_divider(12, 1000, 1000, 500))            #testing with given values in the question