#finding direction of current flow:

current = float(input("Enter current (A): "))

#applying condition to find the direction of current flow
if current > 0:
    print("Current flows from A to B")
elif current < 0:
    print("Current flows from B to A")
else:
    print("No current is flowing")