# Books available in library 

#list of books 
available_books = ['a','b','c','d']
# get input from user 
required_books = input("Enter Name oF Book(s):").lower().split()
# condition 
for book in required_books:
    if book in available_books :
        print(f"{book} availale.")
    else:
         print(f"{book} not available.")


