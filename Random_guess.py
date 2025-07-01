# random guess by user 

import random 

numbers = list(range(1,11))
random_number = random.choice(numbers)

user = int(input("Enter Which Number is Going To Display Between 1 to 10? :" ))

print(f"The Random Number is {random_number}")

if random_number == user:
   print("Your Guess is Correct.")
else:
   print("Your Guess is Not Correct.")
   

