#Calculate Age
print("***This program can tell your age by asking birth year as user input***")

def cal_age():
	year_now = 2019
	year_input_text = input("Enter your birth year: ")
	year_input = int(year_input_text)
	birth_year = year_now - year_input
	return "Your age is " + str(birth_year) 
age_result = cal_age()
print(age_result)
