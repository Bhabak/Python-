#Disctionary Comprehension
#syntax --> {key_expression: value_expression for item in iterable if condition}

# WAP that takes a dictionary of student names and their grades, and creates a new dictionary contsining only the  students who passed the exam (grade 50 or above).

#creating a student dictionary
Student_Names = {'santosh' : 30,'Ramesh' : 40,'Prithak' : 80,'toya' : 20,'riya' : 91}
#Passed students grade>=50
Passed_Students = {name:grade for name,grade in Student_Names.items() if grade>=40}

print(Passed_Students)
