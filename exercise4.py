# question 1: using a for loop with a list
fruits = ["blueberry","peach","strawberry","banana"]
for fruit in fruits:
 print(fruits)

# question 2: using a while loop for countdown
countdown = 5
while countdown >= 1:
  print(countdown)
  countdown -= 1

# question 3: using a for loop with range()
for square_numbers in range(1, 11):
  print(square_numbers **2)

# question 4: using the random module
import random
colors = ["red","blue","pink","purple","green"]
for color in colors:
  picked_color = random.sample(colors, k=3)
  print(picked_color)

# question 5: creating and using a custom module
import math_operations
print(math_operations.add(6, 9))
print(math_operations.subtract(6, 9))
print(math_operations.multiply(6, 9))
print(math_operations.divide(6, 9))
print(math_operations.divide(6, 0))

# calculator program is in math_operations.py file