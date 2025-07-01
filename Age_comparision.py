# Age comparision 

# get data through user

name1,name2 = map(str,input("Enter Your Name separated by space:").split())
age1,age2 = map(int,input("Enter Your Age Seperated By space: ").split())

# condition 
if age1 > age2 :
    print(f"{name1} is big") 
elif age1 < age2 :
    print (f"{name2} is big ")
else: 
    print(f"{name1} and {name2} are at same age ")
    

