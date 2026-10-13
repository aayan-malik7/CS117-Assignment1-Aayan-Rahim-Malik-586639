#Logic Gates

a =int(input("Enter A: "))
b =int(input("Enter B: "))

#we will use OR because in OR condition if one condition is true it runs so here
if (a != 0 and a != 1) or (b != 0 and b != 1):
    print("Bits must be 0 or 1")

else:
    #AND gate gives 1 only if all of its input are 1. If any input is 0, the output is 0
    if a == 1 and b == 1:
        and_output = 1
    else:
        and_output = 0

    #OR gate gives 1 if at least one of its input is 1. It only gives 0 if all inputs are 0
    if a == 1 or b == 1:
        or_output = 1
    else:
        or_output = 0

#XOR gate gives 1 only if the inputs are different. If both inputs are same  the output will be 0
    if a != b:
        xor_output = 1
    else:
        xor_output = 0

    print("AND =", and_output)
    print("OR =", or_output)
    print("XOR =", xor_output)