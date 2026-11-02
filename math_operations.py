def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

print("calculator program")
while True:
  print("enter 1 to add")
  print("enter 2 to subtract")
  print("enter 3 to multiply")
  print("enter 4 to divide")
  print("enter 5 to exit")
  function=int(input("enter your choice:"))
  num1=float(input("enter first number:"))
  num2=float(input("enter second number:"))
  if (function==1):
    print(f"result: {num1} + {num2} = {add(num1,num2)}")
  elif (function==2):
    print(f"result: {num1} - {num2} = {subtract(num1,num2)}")
  elif (function==3):
    print(f"result: {num1} * {num2} = {multiply(num1,num2)}")
  elif (function==4):
    print(f"result: {num1} / {num2} = {divide(num1,num2)}")
  elif (function==5):
    print("bye bye")
    break
  else:
    print("input invalid")
