# Age Calculator


date_of_birth = int(input("Enter Your Birth Date In YYYY Format:")) #users date

# present date 
from datetime import datetime
current_date = datetime.now().year

# calculation 

age = current_date - date_of_birth

print(f"Your Current Age is:{age} ")



