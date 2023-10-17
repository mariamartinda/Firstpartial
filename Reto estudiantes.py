#https://replit.com/@MariaMartin8/Challenge?s=app
print("Hi! this is a program to help you evaluate online purchases")
print("Please enter your purchase amount")
purchase_amount = float(input())
print("Do you have a membership card?")
membership = input()
if purchase_amount>=100 and membership == "yes":
  discount10= purchase_amount * 0.10
  discount=purchase_amount-discount10
  final_disc=discount*0.05
  total_disc=discount-final_disc
  print("We applied a 10% for having a purchase amount greater or equal to a $100 and a 5% extra for having a membership card")
  print("Your total is",total_disc)
elif purchase_amount<100 and membership == "yes":
  discount5=purchase_amount*(5/100)
  finaldisc=purchase_amount-discount5
  print("You got a 5% discount off for having a membership card!")
  print("Your total is",finaldisc)
else:
  print("No additional discount was applied")
  print("Your total to pay is",purchase_amount)
