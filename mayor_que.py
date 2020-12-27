A_number = int( input("Type number A: "))
B_number = int( input("Type number B: "))

if A_number > B_number:
    print("Number A was bigger, its value is:" , A_number)
elif A_number < B_number: 
    print("Number B was bigger, its value is:" , B_number)
else:
    print("both numbers were equal, its value is:", A_number)