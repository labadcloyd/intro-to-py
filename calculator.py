num1Input = float(input("Enter First Number:"))
operatorInput = input("Enter Operator:")
num2Input = float(input("Enter Second Number:"))

def calculate(num1, operator, num2):
	if(operator == "+"):
		return num1 + num2
	elif(operator == "-"):
		return num1 - num2
	elif(operator == "/"):
		return num1 / num2
	elif(operator == "*"):
		return num1 * num2
	else:
		return "invalid input"

print(calculate(num1Input, operatorInput, num2Input))