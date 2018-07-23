def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def mul(x, y):
	return x * y
	
def div(x, y):
	return x / y

def main():
	print("Hello!")
	operation = input("What would you like to do?(+,-,*,/) ")
	if(operation != '+' and operation != '-' and operation != '*' and operation != '/'):
		print("Error. Try again...")
	else:
		x = int(input("Enter number x: "))
		y = int(input("Enter number y: "))
		if(operation == "+"):
			print(add(x, y))
		elif(operation == "-"):
			print(sub(x, y))
		elif(operation == "*"):
			print(mul(x, y))
		else:
			print(div(x, y))
main()