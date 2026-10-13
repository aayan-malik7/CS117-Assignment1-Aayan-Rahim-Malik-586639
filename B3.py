# Sensor Readings

#the vriable is containing all the the voltage readings
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)   

above_count= 0
highest = readings[0]           # Assuming that the 1st reading is the highest (reference)
lowest = readings[0]               # Assuming that the 1st reading is the lowest (reference)
total = 0                     
for reading in readings:
    if reading > 3.2:                       # Check if the reading is greater than 3.2 V
        above_count = above_count + 1
        
    if reading > highest:                   # Check if the  voltage reading is higher than our voltage maximum
        highest = reading
        
    if reading < lowest:                    # Check if the` voltage` reading is lower than our  voltage minimum
        lowest = reading
        
    total = total + reading                 # Add the voltage reading to the  total
    
# Calculate the average by dividing the total sum by the total number of readings
average = total / len(readings)            #len() function returns the number of items in a tuple

print("Readings above 3.2 V:", above_count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", round(average, 1), "V")       #round() function rounds the average to 1 decimal places