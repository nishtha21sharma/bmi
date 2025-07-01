def calculate_bmi():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You're underweight.")
    elif bmi < 24.9:
        print("You're healthy.")
    elif bmi < 29.9:
        print("You're overweight.")
    else:
        print("You're obese.")

calculate_bmi()
