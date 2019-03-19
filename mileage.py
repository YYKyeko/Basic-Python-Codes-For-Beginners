print("how many kilometers do you want to convert: ")
kms = input()
miles = float(kms) / 1.60934
miles = round(miles, 2)
print(f"Your {kms} kilometers equal to {miles} miles ")
