#Tip Calculator

Total_bill = float(input("What was the total bill? "))
Tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
Number_of_people = int(input("How many people to split the bill? "))

payment_per_person = round(
    (Total_bill / Number_of_people) * (1 + Tip_percentage / 100), 2)
final_payment = "{:.2f}".format(payment_per_person)
print(f"Each person is going to pay ${final_payment} for the meal")
