# Loop are to iterate through data that are iteratable, those data consist of strings, integer, floats
# There are two types of loops:
# For loops
string = input("Enter your name: ") # Trang
for char in string:
  print(char)

for i in range(3):
  print(i)

# While loops
i = 10 # In a while loop, a counter variable is almost always need to be declared
while i > 0: # The loop will stop after a certain condition is met with the a counter variable
  print(i)
  i = i - 1

while True: # This loop is performing an infinite looping
  i = i - 1
  if i == 9:
    break # We always need a if-else condition to break the loop, else the program will be ran infinitely

# For loop can perform actions that while loop can, however, while loops don't always have the ability to perform for loop action
# While loop are almost always used to perform infinite looping

