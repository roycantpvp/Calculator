while True:
  try:
    x = int(input("Enter your first number: "))
    break

  except ValueError:
      print("Please input integer only...")  
      continue

op = input("Enter your operator: ");

while True:
  try:
    y = int(input("Enter your second number: "))
    break

  except ValueError:
      print("Please input integer only...")  
      continue


def multiply():
    z = int (x) * int (y);
    print(z);
def divide():
    z = int (x) / int (y);
    print(z);
def addition():
    z = int (x) + int (y);
    print(z);
def subtract():
    z = int (x) - int (y);
    print(z);

def calculate():
    if op == "*":
        multiply();
    elif op == "/":
        divide();
    elif op == "+":
        addition();
    elif op == "-":
        subtract();
    elif op != "+" or "-" or "/" or "*":
        print("incorrect operator")

calculate();
     
