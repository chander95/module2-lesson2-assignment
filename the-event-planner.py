#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

#BUGGY CODE

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
additionals = "audio system" if venue == "large hall" else "projector"

vegetarian = input("Would you like vegetarian food? Yes or No ")
food = "Veggie Delight Caterers" if vegetarian == "Yes" else "Gourmet Meals Caterers"

print(venue)
print(additionals)
print(food)

#Task 2: Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

#Task 3: Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".