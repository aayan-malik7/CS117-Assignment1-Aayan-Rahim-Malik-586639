#Star-Delta (Y-Δ) Transformation

# Defining a function to convert Star resistors into delta resistors 
def star_to_delta(ra, rb, rc):                  # ra, rb, rc are the 3 resistors of star network
    
    numerator = ra * rb + rb * rc + rc * ra     # Calculating the sum of all pairwise products of the star resistors used as the numerator for all formulas

    rab = numerator / rc
    rbc = numerator / ra                           #these are the formulas for calculating delta resistances
    rca = numerator / rb


    return round(rab, 2), round(rbc, 2), round(rca, 2)              # return the 3 delta resistances 

print("star_to_delta(10, 20, 30) ->", star_to_delta(10, 20, 30))    # testing with the given values