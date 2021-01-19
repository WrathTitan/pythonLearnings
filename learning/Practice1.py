'''
	Simple program for telling the year the user turns 100 years old
'''
name=input("Enter your Name: ") 	#input() function used
age=int(input("Enter your Age: "))	#type conversion using int() function
year=2021+(100-age)			#logic
print("Welcome",name,"you will turn 100 years old in the year",year)	#print statement
