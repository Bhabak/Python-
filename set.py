#Making a set of my and friend's hobbies.Challange is to Add some hobbies and remove one and then make union and intersection portion

#My Hobbies
My_Hobbies = {"Football", "Singing" , "Reading"} 
#Adding Hobbies
My_Hobbies.add("Cooking")
My_Hobbies.add("Travelling")
#Remove one hobby
My_Hobbies.remove("Singing")
#friend's hobbies
Friend_Hobbies = {"Singing","Reading" ,"Travelling",}

#union 
union = My_Hobbies.union(Friend_Hobbies)
#Intersection
Intersection = My_Hobbies.intersection(Friend_Hobbies) 

#Display 

print("My_Hoobies:",My_Hobbies)
print("Friends_Hobbies:",Friend_Hobbies)
print("Union:",union)
print("Intersection",Intersection)

