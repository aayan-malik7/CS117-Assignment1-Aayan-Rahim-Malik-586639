#Continuous Discharge Analysis

#list of voltage readings given per mint
voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

#For storing best steak
best_streak = 1
best_start = voltages[0]
best_end = voltages[0]

#for storing current streak
current_streak = 1
current_start = voltages[0]

for i in range(1, len(voltages)):                       #loop through the readings
    if voltages[i] < voltages[i - 1]:                   #Check the voltage drop compared to the previous minute
        current_streak = current_streak + 1                    #increase the lenghth of current decreasing streaks
    else:
        #decreasing streak is broken, so start new one
        current_streak = 1
        current_start = voltages[i]

    #check if the current streak is longer than the longest streak
    if current_streak > best_streak:
        best_streak = current_streak
        best_start = current_start
        best_end = voltages[i]

print("Longest continuous drop:", best_streak, "minutes")
print("Started at:", best_start, "V")
print("Ended at:", best_end, "V")