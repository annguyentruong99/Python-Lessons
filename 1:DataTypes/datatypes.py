"""
Data type and operators
There are a a couple main data types in Python:
1. Text type: str
2. Numeric type: int, float
3. Sequence type: list, tuple, range
4. Mapping type: dict
5. Boolean type: True, False
"""

# 1: text type
# Anything that goes in to this "" or '' is a string
# E.g:

"Hello Trang Beo"
"3"
"4"
"Du ma"
# You can use the print() fundtion to display the string in the console
# String is a immutable data, meaning you cannot change its content once it's being declared
# You can concadinate, meaning you can add two or more strings together using the + operator
# E.g:
print("An is " + "awesome :D")
# This prints: An is awesome :D 

# 2: Numeric type
# Integer or decimal (float) numbers 
# E.g (int):
3
2
6
146862493
8758146
1
-1545
-7
#E.g (float):
1.45
2.6567
716249.2356
"""
You can use math operators for calculations in Python
Some basic operators:
1. Addition: +
2. Subtraction: -
3. Multiplication: *
4. Division: /
5. Exponential: **

There are also some special operators:
1. Remainder: % 
This operator returns the remainder of a division (eg: 4 % 3 = 1)
2. Assignment operator: =
This operator is use to declare a variable (eg: x = 3)
3. Comparision operators: 
  a, == : This is to check if two data is equal, if they do return True, else returns False
  b, > : This is to check if a data is bigger
  c, < : This is to check if a data is smaller
  d, >= : This is to check if a data is bigger or equal
  e, <= : This is to check if a data is smaller or equal
  f, != : TThis is to check if two data is not equal, if they do return True, else returns False
"""

"""
*** Data can be given a name, in coding, the name that stores a data is called variable
*** Some popular naming conventions for variables are camelcase (e.g: helloWorld, numberList, walkDist, etc.) or words seperated by _ (e.g: hello_word, number_list, walk_dist).
*** Choose a convention to be your preferred and stick to it. Naming should be short, simple, and make sense
"""



# 3: Sequence type
  # A list is a data type used to store collection of data, it is declared by using square brackets []
  # Items in a list are ordered, changable, and allow duplicated values. They are also indexed, first item in a list has a index of 0
  # E.g:
    numList = [1,2,3,4,5,6,7] # This is a integer list
    strList = ["Hello", "Hi", "Goodbye"] # This is a string list
    aList = [1,"Blah Blah", 231, 48, "Cups"] # You can have a combination of data types in a list
    # Access an item of the list by calling the item's index
    print(numList[0]) # Returns 1
    print(aList[1]) # Returns "Blah Blah"
    print(strList[-1]) # Returns the last element of the list, "Goodbye"
    print(numList[0:3]) # Return [1,2,3,4]
    # A list is changable since we can change, add, or remove items the list
    # Some popular built-in funtions to work with list:
      numList.append(10) # Add 10 to the end of numList ** This is the one I use a lot in projects
      numList.clear() # Remove all the items in a list
      print(numList.sort()) # Sort the list in ascending order or alphabetically
      len(numList) # Return the number of element in a list


  # A tuple shares most its traits with a list, except it's unchangable, it is declared by using round brackets ()
  # Items in a tuple are also indexed, first item in a tuple has a index of 0.
  # E.g:
    numTup = (1,2,3,4,5,6)
    strTup = ("Hello", "Hi", "Goodbye")
    aTup = (1,"Blah Blah", 231, 48, "Cups")
    # Access an item of the tuple by the same way you access item in a list

  # A dictionary is used to store data in key:value pair, and is declared by curly brackets {}
  # Dictionary items are changable, unordered, and does not allow duplicate
  # E.g:
  employeeInfo = {
    "Name": "Trang Phan",
    "Age": 23,
    "Graduated": True,
    "Married": False,
    "Hobbies": ["Eat", "Sleep", "Repeat"]
  }
  # To access a value in dictionaries, key name should be referred since dictionaries are unordered.
  print(employeeInfo["Name"]) # Return "Trang Phan"
  print(employeeInfo["Hobbies"]) # Return ["Eat", "Sleep", "Repeat"]


stupidList = [[1,2,6,2,6,1,62,123,[1,2,64,54,121,1]], [1,2,6,162,362,123]]
print(stupidList[1][4]) # return 362
print(stupidList[0][-1][4]) # return 121

print(22 / 2 )


bool(2)