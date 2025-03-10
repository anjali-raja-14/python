def user_information():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    feet = int(input("Enter your height in feet: "))
    inches = int(input("Enter your height in inches: "))
    user_weight = float(input("Enter your weight (kg): "))

    # Convert height to meters
    Height_in_meters = (feet * 0.3048) + (inches * 0.0254)
    print(f"Height in meters: {Height_in_meters:.2f}")

    # Calculate BMI
    user_bmi = user_weight / (Height_in_meters ** 2)

    # Print BMI with 2 decimal places
    print(f"BMI: {round(user_bmi, 2)}")

user_information()
# request module