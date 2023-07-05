# Implement a Python function called find_factorial that takes a positive integer as input and calculates its factorial using a while loop. Use the pass keyword to handle the case when the input is zero.


def find_faqctorial():
	num = int(input("Enter a positive integer: "))
	factorial = 1
	for i in range(1,num + 1):
		factorial *= i
	print("The factorial of", num, "is:", factorial)
find_faqctorial()





# Write a Python program that prints all the prime numbers between 1 and 100 using a for loop and the break keyword.



for num in range(1,100):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			print(num)




# Implement a Python program that asks the user to enter a password. If the password matches a predefined secret password, display a success message. Otherwise, display an error message using an if/else ternary expression.




secret_password = "123nn?"
user_password = input("Enter the password: ")
if user_password == secret_password:
	print("Success!") 
else:
	print("Error: Invalid password.")




# Create a Python function called print_pattern that takes an integer as input and prints the following pattern using a while loop:



def print_pattern(n):
	i = 1
	while i <= n:
		print("*" * i)
		i += 1
print_pattern(4)



# Write a Python function called find_common_elements that takes two lists as input and returns a new list containing the common elements between the two input lists. Use a for loop and an if statement to check for common elements.


def find_common_elements(lst1,lst2):
	common_element = []
	for i in lst1:
		if i in lst2:
			common_element.append(i)
	return common_element
lst1 = [1,8,15,47,96]
lst2 = [15,96,5,36,47]
result = find_common_elements(lst1,lst2)
print(result)



# Implement a Python function called find_prime_factors that takes a positive integer as input and returns a list of its prime factors. Use a while loop and an if statement to find and add prime factors to the list.


def find_prime_factors(n):
	factors = []
	i = 2
	while i <= n:
		if n % i == 0:
			factors.append(i)
			n //= i
		else:
			i += 1
	return factors
result = find_prime_factors(95)
print(result)



# Create a Python program that simulates a basic calculator. It should repeatedly ask the user for two numbers and an operator (+, -, *, /) and perform the corresponding operation using if/elif statements. Use a while loop to allow the user to perform multiple calculations until they choose to exit.


def calculator():
	while True:
		print("Calculator")
		print("Enter '+' for addition")
		print("Enter '-' for subtraction")
		print("Enter '*' for multiplication")
		print("Enter '/' for division")
		print("Enter 'exit' for quit")
		operator = input("Enter the operator: ")
		if operator == 'exit':
			print("Exiting the calculator.")
			break
		if operator not in ['+','-','*','/']:
			print("Invalid operator. Please try again.")
			continue
		try:
			n1 = float(input("Enter the first number: "))
			n2 = float(input("Enter the second number: "))
		except ValueError:
			print("Invalid number. Please try again.")
			continue
		if operator == '+':
			result = n1 + n2
		elif operator == '-':
			result = n1 - n2
		elif operator == '*':
			result = n1 * n2
		elif operator == '/':
			if n2 != 0:
				result = n1 / n2
			else:
				print("Division by zero is not allowed.")
				continue
		print("Result",result)
		print()
calculator()











