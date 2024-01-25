# Enter your height in meters e.g., 1.55
height = float(input("what is your height in meters? "))
# Enter your weight in kilograms e.g., 72
weight = int(input("what is your weight in kilograms? "))
# Calculate the BMI
bmi = weight/height**2

if bmi < 18.5:
  print(f"Your BMI is {bmi:.1f}, you are underweight")
elif bmi > 18.5 and bmi < 30:
  print(f"Your BMI is {bmi:.1f}, you are normal")
elif bmi >= 25 and bmi < 30:
  print(f"Your BMI is {bmi:.1f}, you are slightly overweight")
elif bmi >=30 and bmi < 35:
  print(f"Your BMI is {bmi:.1f}, you are obese")
elif bmi >= 35:
  print(f"Your BMI is {bmi:.1f}, you clinically obese")  ###bmi:.1f approximates to the nearest 1 decimal