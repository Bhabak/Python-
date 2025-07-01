# weekly expences 

Sunday_exp      = 1000
Monday_exp      = 1500
Tuesday_exp     = 4000
Wednesday_exp   = 500
Thursday_exp    = 600
Friday_exp      = 200
Saturday_exp    = 200

#calculation part 

Total_exp = Sunday_exp + Monday_exp + Tuesday_exp + Wednesday_exp + Thursday_exp + Friday_exp + Saturday_exp
Average_exp = Total_exp//7

#Display
print(f"Total expences in a week is {Total_exp}")
print(f"Average expences in a week is {Average_exp}")
