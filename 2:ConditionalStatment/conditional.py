# Conditional statement (if-else) statement is used to check whethere a certain condition(s) are met 
# We can have 1 or more conditions in an if statement
# If there are 2 or more conditions in an if statement, and/or are used
# and: to check whether 2 or more conditions are met 
# or: to check whether 1 of the 2 or more conditions are met

# E.g:

number = int(input("Enter your number: "))
if (number % 2 == 0) or (number != 0):
  print("This is an even number")
elif (number % 2 == 1) and (number != 0):
  print("Odd")