#bmi calculator
height=float(input("Enter your height(meter): "))
weight=float(input("Enter your weight(kg):" ))
BMI=weight/(height**2)
print(BMI)
if BMI<18.5:
    print(" Thinness")
elif BMI > 18.5 and BMI < 25:
    print("Normal")     
elif BMI > 25 and BMI < 30:
    print("overweight")     
else:
    print("excess weight ")    