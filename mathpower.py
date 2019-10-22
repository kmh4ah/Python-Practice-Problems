#################### MATH POWER ################################
#First Method: Creating own function to get a power of an entered number
print("***This program can tell the power of an entered number***")
base_num = int(input("Enter a base number: "))
power_num = int(input("Enter a power number: "))
def power(base_value, power_value):
	result = base_num ** power_num   #remember we are trying to do some calculation here #based on the numbers enterd by the user 
	return result
result = power(base_num,power_num)
print(result)


#Second Method: Applying built-in function called pow() to get the result
print("Using pow() function as an alternative: ", pow(4,3))

print("\n")

