#expenditure of a week 

weekly_expences = {
    "Sunday"    : 100,
    "Monday"    : 200,
    "Tuesday"   : 300,
    "Wednesday" : 400,
    "Thursday"  : 500,
    "Friday"    : 600,
    "Saturday"  : 700
}

#Calculation part
total= sum(weekly_expences.values())
average = total/ len(weekly_expences)

#Display part 
print(f"\n#### Spending ####\n")
for day, amount in weekly_expences.items(): print(f"{day}:{amount} units")
print(f"\nTotal Expences is {total}")
print(f"Average Expences is{average:.0f} \n")