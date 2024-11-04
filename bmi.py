weight=float(input("Enter your weight: "))
height=float(input("Enter your height(feet): "))
height_meter=height/3.28084
BMI=(weight/height_meter**2)
round_bmi=round(BMI,2)
round_height_meter=round(height_meter,2)
if(BMI<16.0):
    print(f"Your BMI is {round_bmi} and You are Underweight (Severe Thinness)")
elif(BMI>16.0 and BMI<16.9):
    print(f"Your BMI is {round_bmi} and You are Underweight (Moderate Thinness)")
elif(BMI>17.0 and BMI<18.4):
    print(f"Your BMI is {round_bmi} and You are Underweight (Mild Thinness)")
elif(BMI>18.5 and BMI<24.9):
    print(f"Your BMI is {round_bmi} and You are under Normal Range")
elif(BMI>25.0 and BMI<29.9):
    print(f"Your BMI is {round_bmi} and You are Overweight (Pre-Obese)")
elif(BMI>30.0 and BMI<34.9):
    print(f"Your BMI is {round_bmi} and You are Obese (Class I)")
elif(BMI>35.0 and BMI<39.9):
    print(f"Your BMI is {round_bmi} and You are Obese (Class II)")
elif(BMI>45.0):
    print(f"Your BMI is {round_bmi} and You are Obese (Class III)")





