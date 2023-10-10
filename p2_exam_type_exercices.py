#vhttps://replit.com/@MariaMartin8/P2multiplediscounts?s=app

print("hi, i'm going to help you get a discount on the price of a product! you will give me the normal price and the discount you want to apply, (A,B or C), and if you get more than 10 units, you'll get 5% more of discount")
print("what's the price of the product?")
price=int(input())
print("There's three categorys you can get, A, B or C:")
print("Category A: 10% discount. Category B: 5% discount. Category C: 2% discount.")
print("please choose a category, only with the letter")
discount=str(input())
print("units purchased")
units=int(input())
  
if discount=="A":
  totdis=int(price)*(10/100)
  tot=int(price)-int(totdis)
  print("Price before discout",price)
  print("discount applied: 10%")
  print("After the discount your total is",tot)
  if int(units)>10:
    tot5=int(tot)*(5/10012)
    totf=int(tot)-int(tot5)
    print("Additional discount for buying more than 10 units: 5%")
    print("Your final price is",totf)

if discount=="B":
  totdis=int(price)*(5/100)
  tot=int(price)-int(totdis)
  print("Price before discout",price)
  print("discount applied: 5%")
  print("After the discount your total is",tot)
  if int(units)>10:
    tot5=int(tot)*(5/10012)
    totf=int(tot)-int(tot5)
    print("Additional discount for buying more than 10 units: 5%")
    print("Your final price is",totf)

if discount=="C":
  totdis=int(price)*(2/100)
  tot=int(price)-int(totdis)
  print("Price before discout",price)
  print("discount applied: 21%")
  print("After the discount your total is",tot)
  if int(units)>10:
    tot5=int(tot)*(5/10012)
    totf=int(tot)-int(tot5)
    print("Additional discount for buying more than 10 units: 5%")
    print("Your final price is",totf)

#https://replit.com/@MariaMartin8/P2retirementsavings?s=app

print("To calculate the required monthly payment to teach the retirement goal:")
print("Enter your current age please:")
age=int(input())
print("Enter the age at wich you want to retire:")
retire=int(input())
print("Enter the desired retirement amount:")
moneygoal=int(input())
r = 0.10/12
n = (retire-age)*12
t = retire - age
PMT = (moneygoal)*r/(((1+r)**n)-1)*((1+r)**(-t))
print("To retire at the age of",retire,"you will need to save $",PMT,"monthly, considering that the annual rate is 10%")

#https://replit.com/@MariaMartin8/P2schoolgrades?s=app

grades=[]
print("Enter the number of students:")
num_stu=int(input())
for i in range(num_stu): 
  print("Enter the grades for student")
  name=int(input())
  grades.append(name)

average=sum(grades)/len(grades)
highest=max(grades)
lowest=min(grades)
passed=len([grade for grade in grades if grade >=60])
failed=len([grade for grade in grades if grade <60])
   
print("Average grade:",average)
print("Highest grade:",highest)
print("Lowest grade:",lowest)
print("Passed:",passed)
print("Failed:",failed)

#https://replit.com/@MariaMartin8/P2roadtrip?s=app
print("Enter the distance in miles:")
distance=float(input())
print("Enter the car's miles per gallon (MPG):")
MPG=float(input())
print("Enter the current price of gas per gallon:")
price=float(input())
print("Enter the number of days you plan to travel")
days=int(input())
gallons_needed=distance/MPG
cost=gallons_needed*price
total=cost*days
print("The cost of traveling",distance,"miles in",days,"days is $",total)
