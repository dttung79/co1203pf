height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

BMI = weight / (height ** 2)
print(f'Your BMI is {BMI:.2f}')

if BMI < 18.5:
    print('Underweight')
elif BMI < 24.9:
    print('Normal weight')
elif BMI < 29.9:
    print('Overweight')
else:
    print('Obesity')