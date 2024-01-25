###conditional statements

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("What is your age? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age < 12:
#       bill = 5
#       print("youth tickets are $5")
#     elif age <= 18:
#       bill = 7
#       print("youth tickets are $7")
#     else:
#       bill = 12
#       print("adult tickets are $12")
#     wants_photo = input("Do you want your pictures taked? Y or N? ").upper()
#     if wants_photo == "Y":
#       bill+=3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

##pizza order
size = input("What size would you like? S, M, or L? " ).upper()
bill = 0
if size == "S":
  bill = 15
  want_pepperoni = input("Do you want pepperoni? Y or N? ").upper()
  if want_pepperoni == "Y":
    bill+=2
  want_cheese = input("Do you want extra cheese? Y or N? ").upper()
  if want_cheese == "Y":
    bill+=1
    print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is: ${bill}.")
  else:
    print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is: ${bill}.")
elif size == "M":
  bill = 20
  want_pepperoni = input("Do you want pepperoni? Y or N? ").upper()
  if want_pepperoni == "Y":
    bill+=3
  want_cheese = input("Do you want extra cheese? Y or N? ").upper()
  if want_cheese == "Y":
    bill+=1
    print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is: ${bill}.")
  else:
    print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is: ${bill}.")
elif size == "L":
  bill = 20
  want_pepperoni = input("Do you want pepperoni? Y or N? ").upper()
  if want_pepperoni == "Y":
    bill+=3
  want_cheese = input("Do you want extra cheese? Y or N? ").upper()
  if want_cheese == "Y":
    bill+=1
    print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is: ${bill}.")
  else:
    print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is: ${bill}.")
