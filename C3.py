#Decimal to Binary

def decimal_to_binary(n):       # Defining a function that converts a decimal number into its binary string representation
    if n == 0:                  # 0 is special case in which loop will skip it and return an empty string

        return "0"
    binary = ""
    
    while n > 0:                    #dividing by 2 until nothing is left
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
        
    return binary                   #Return the binary string

print("decimal_to_binary(20) ->", decimal_to_binary(20))  #Testing the function with number 20

print("decimal_to_binary(35) ->", decimal_to_binary(35))  #Testing the function with number 35