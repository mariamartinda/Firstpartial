#round one addition and substraction
def addition(a,b):
  x = a + b
  return x

def substraction(a,b):
  x = a - b
  return x

print("Give me your first number:")
a = int(input())
print("Give me your second number")
b = (int(input()))
print("The result from the addition is", addition(a,b), "and from the substraction", substraction(a,b))

#round 2 multiplication and division
def multiplication(a,b):
  x = a * b
  return x

def divison(a,b):
  x = a/b
  return x

print("Give me your first number")
a=int(input())
print("Give me the second number please")
b=int(input()) 
print("the result of the multiplication is",multiplication(a,b), "and the total of the division is",divison(a,b))

#round three conversion km to m
def conversion():
  print("How many kilometers have passed?")
  km=int(input())
  m=km/1000
  return m
m=conversion()
print("The result in meters is",m)

#round four area
def triangle_area():
  print("What is the base of your triangle?")
  b=int(input())
  print("What is the height of the triangle?")
  h=int(input())
  a=(b*h)/2
  return a
  a=triangle_area()

print("The area of your triangle is:",triangle_area())
