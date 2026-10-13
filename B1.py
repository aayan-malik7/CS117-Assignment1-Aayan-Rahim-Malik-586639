#current through  10 ohm resistor when V=1 V to 10 V

resistance = 10     #we have the fixed resistance


#Instead of applying ohms law again and again  we will use for loop

for voltage in range(1, 11):       #Specifying the Voltage range from 1 to 10 volts
    current = voltage / resistance     #formula

    print("V =", voltage, "V, I =", current, "A")