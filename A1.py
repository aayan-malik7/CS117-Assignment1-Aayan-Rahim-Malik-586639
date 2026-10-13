#checking whether the fuse will blow or not
voltage = float(input("Enter voltage: "))
resistance = float(input("Enter resistance: "))

if resistance <= 0:
    print("Invalid resistance")
else:
    #Applying  I =V/R formula
    current = voltage / resistance
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")