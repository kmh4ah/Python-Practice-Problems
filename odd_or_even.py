#Enter a number and check if the entered number is 'odd' or 'even'
print("***This program can differentiate if entered number is 'odd' or 'even'***")
num_input = int(input("Enter a number: "))
if num_input % 2 == 0:
	print(str(num_input) + " is an even number.")
else:
	print(str(num_input) + " is an odd number.")
