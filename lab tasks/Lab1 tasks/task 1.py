weight = float(input("enter the weight of person in kg: "))
height = float(input("enter the height of the person: "))

BMI = weight / (height ** 2)
BMI = round(BMI, 2)
print("BMI is:", BMI)
if BMI < 18.5:
    print("underweight")
elif BMI >= 18.5 and BMI < 24.9:
    print("normal weight")
elif BMI >= 25 and BMI < 29.9:
    print("overweight")
else:
    print("obese")
