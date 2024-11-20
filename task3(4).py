#Write a python program to find the sum of first and last digit of an integer
number=1289 # assign th int to the variable
#convert the int to string using str() for indexing and slicing
number=str(number)
#number[0]--->first character from the string
first_digit=int(number[0])
#number[-1]--->last character from the string
last_digit=int(number[-1])
addition=first_digit+last_digit
print(addition)