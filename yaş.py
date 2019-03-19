age = input("how old are you: ")
age = int(age)
if age >= 2 and age <= 8:
    print("you pay 2 dollar.")
elif age >= 65:
    print("you pay 5 dollar.")
else:
    print("you pay 10 dollars.")
