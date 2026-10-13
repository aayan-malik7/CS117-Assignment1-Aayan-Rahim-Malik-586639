#digits for the 1st band colour of a resistor

colour = input("Enter band colour: ").lower()

#we will elif because we have multiple conditions
if colour == "black":
    print("Digit = 0")
elif colour == "brown":
    print("Digit = 1")
elif colour == "red":
    print("Digit = 2")
elif colour == "orange":
    print("Digit = 3")
elif colour == "yellow":
    print("Digit = 4")
elif colour == "green":
    print("Digit = 5")
elif colour == "blue":
    print("Digit = 6")
elif colour == "violet":
    print("Digit = 7")
elif colour == "grey":
    print("Digit = 8")
elif colour == "white":
    print("Digit = 9")
else:
    print("Invalid colour")