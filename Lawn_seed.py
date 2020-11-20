def seed(square_feet):
    # 1 pound of seed for evey 500 square feet
    amount = square_feet / 500
    amount = round(amount, 1)
    return amount



def fertilizer(square_feet):
    amount = 3 * square_feet
    amount = round(amount, 1)
    return amount



def accurate_fertilizer(square_feet):
    amount = 3 * (square_feet / 500)
    amount = round(amount, 1)
    return amount

def labor(square_feet):
    time = square_feet / 1000
    time = time * 5
    time = round(time, 1)
    return time

def water(square_feet, inches):
    # Every acre(43,560 sqft) gets 27,143 gallons of water for every inch of rain
    # That is roughly 0.623 gallons of water per square foot
    water_needed = square_feet * 0.623
    water_needed = water_needed * inches
    water_needed = round(water_needed, 2)
    return water_needed

def seeding_cost(square_feet, inches):
    grass_cost = seed(square_feet) * 10
    
    fert_cost = accurate_fertilizer(square_feet) * 4

    labor_cost = labor(square_feet) * 40
    
    water_cost = water(square_feet, inches) * 0.02
    
    total_cost = grass_cost + fert_cost + water_cost + labor_cost
    # String Formatting total cost to a currency format. This bit of code
    # Allows me to add the "$" directly infront of the total
    # .2 tells python I want two decimal places
    # f tells python its a floating point number
    total_cost = "${:,.2f}".format(total_cost)
    return total_cost

def inches_of_water(days):
    # Water needed every week = 1 inch.
    water_needed = (1/7) * days
    water_needed = round(water_needed, 1)
    return water_needed
    
    


    
    
    
    
    

    

# Get the area of the lawn and the number of days since the last rain from the user

square_footage = float(input("Please type the area of the lawn in square feet.\n"))
days = float(input("How many days has it been since the last rain event?\n"))




# Display to the user how many inches of water are needed since
# it has not rained in the amount of days that they specified
print("Inches of water needed: ", inches_of_water(days), "Inches")


# Disply to the user how much the estimated cost of the project will be
print("The total estimated cost of the project will be: ", seeding_cost(square_footage, inches_of_water(days)))



input("Press <enter> to exit")














    
