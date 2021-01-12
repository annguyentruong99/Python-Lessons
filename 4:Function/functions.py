# A function is a block of code that perform repetitive task in a program
# Codes in a function are only executed when the function is called, data (argurment or parameters) can be passed to the function when called.
# Data can be returned from a function
# E.g:

def print_hello_world(message): # A function is declared with def keyword, any parameters are passed into ()
  return message
# Calling the function
print_hello_world("Hello") # prints Hello, World! to the console

"tao-tai-khoan an.nguyentruong99@gmail.com"

def request_handler(message):
  message = message.split(" ") # return ["tao-tai-khoan", "an.nguyentruong99@gmail.com"]
  command = message[0] # Extract the message execution word
  message = message[1:] # Extract the command's params
  notFound = "Làm gì có cái câu lệnh như thế lày! :grinning: Mời thanh niên chạy /cba huong-dan nếu chưa biết dùng hoặc kiểm tra lại xem có sai sót trong câu lệnh không :grinning:"
  if command == "tao-tai-khoan" and len(message) >= 1: # len = length
    if len(message) == 0:
      return "Chưa có username và/hoặc email của học sinh"
    else:
      email = message[0]
      return register_student(email) # another function
  else:
    return notFound


# There are two types of functions:
# Functions that return a data and functions that don't return anything

# Structure of a program
# Start with a main() function, which is a function that first being called when the program is executed and it usually contains the logics of the program.

def game():
  pass # this is in case you want your function to be left empty, the program will still be run without any errorss


if __name__ == "__main__":
  game()