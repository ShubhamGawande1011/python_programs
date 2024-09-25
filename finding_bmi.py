weight = int(input("Enter the weight in kg: "))  # Corrected unit from km to kg
height = int(input("Enter the height in m: "))

BMI = weight / (height * height)

print(f"The BMI is {BMI:.2f}")  # Display BMI to two decimal places

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal Weight")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obesity")
