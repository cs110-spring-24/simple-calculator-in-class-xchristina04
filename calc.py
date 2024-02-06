num1 = int(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = int(input("Enter another number: "))

if op == "+":
	total = num1 + num2
	print(f"{num1} + {num2} = {total}")
elif op == "-":
	print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
	print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
	print(f"{num1} / {num2} = {num1 / num2}")
elif op == "**":
	print(f"{num1} ** {num2} = {num1 ** num2}")
elif op =="//":
	print(f"{num1} // {num2} = {num1 // num2}")
else:
	print(f"{num1} % {num2} = {num1 % num2}")	