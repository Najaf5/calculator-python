num1 = float(input("First Number: "))
num2 = float(input("2nd number: "))
operator = input("What do you want to do with these numbers?")

if operator == "divide" :
  product=num1/num2
  print(product)


elif operator == "multiply" :
  product = num1 * num2
  print(product)


elif operator == "add" :
  product = num1 + num2
  print(product)


elif operator == "subtract" :
  product = num1 - num2
  print(product)

else:
  print("Please input either divide, multiply, add, or subtract")