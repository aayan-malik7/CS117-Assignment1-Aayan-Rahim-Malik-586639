#current and Power 

def current(v, r):             #Defining function to calculate current using ohms law
    return v / r

def power_dissipated(i, r):         # Defining function to calculate power dissipated in a resistor using  formula P = I^2 * R

    return i ** 2 * r

current_calc = current(12, 6)       #Calculating the current using  12V and 6 Ohms 

power = power_dissipated(current_calc, 6)    #Calculating the power dissipated using the calculated current 6 Ohms resistance

#results
print("Current =", current_calc, "A")
print("Power =", power, "W")