age = input("how old are you: ")


if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("you can join but you must use wristband.")
    elif age > 21:
        print("you can join and you can drink.")
    else:
        print("too young")
else:
    print("please enter an age!")
