"""
Sometimes, you need to work with and get datas from a file

Some popular files that usually used in python projects:
** text files (.txt)
** comma separated values files (.csv)
** javascript object notation files (.json)

To work with a file in Python, first, you have 
to open the file in the appropriate mode using 
"with open("filename", "mode abbreviation") as variable_name":

There are three basic modes that are commonly used in Python:
** read mode - r
** write mode - w
** append mode - a

Example of each modes:
"""

# Read mode: this mode is used to read data from an existing file
with open("helloWorld.txt", "r") as readFile:
  print(readFile.read()) # This built-in function read the whole file as one big string
  print(readFile.readline()) # This built-in function only read the first line of the file
  print(readFile.readlines()) # This built-in function put each line into a list

# Write mode: this mode is used to write data to either an existing or new file
# With existing files, this mode with replace any existing string, it will create a new file if the file stated hasn't existed yet.
with open("helloWorld.txt", "w") as writeFile:
  writeFile.write("Hello, Trang :D") # This function is to replace any string in the existing file
  writeFile.writelines(["Hello ", "Trang ", ":D"]) # This function is to replace any string in the existring file, starting from element indexes 0


# Append mode: this mode is used to add data to either an existing or new file
# With existing file, this mode will add the data to the end of the file, it will create a new file and add the data if the file hasn't existed yet.
with open("hello.txt", "a") as appendFile:
  appendFile.write("Hello")
  appendFile.writelines(["Hello", "Trang"])
