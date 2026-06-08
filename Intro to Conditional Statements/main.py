#challenge 1

userName = str(input(f"What is your name?"))
print(f"Hello {userName}")

if (userName == "haruhisa"):
  print("Hey there!")
  print("Tonight, play less video games and go to bed at a good time")
else:
  print("Go away")

#challenge 2

num1 = str(input(f"Please enter the number"))
num2 = str(input(f"Please enter a different value than before"))
if (num1 >= num2):
  print(f"{num1} is bigger")
else:
  print(f"{num2} is bigger")

#dhallenge 3

num1 = str(input(f"Please enter the number"))
num2 = str(input(f"Please enter a different value than before"))
if (num1 >= num2):
  print(f"{num2} is smaller")
else:
  print(f"{num1} is smaller")
  
#challenge 4

print(f"What is the answer to this? 59*61")
num1 = int(input(f"Please answer"))
if (num1 != 3599):
   print(f"{num1} is  mistake.")
else:
   print(f"{num1} is correct!")
  
print(f"What is the answer to this? 98*67")
num1 = int(input(f"Please answer"))
if (num1 != 6566):
   print(f"{num1} is  mistake.")
else:
   print(f"{num1} is correct!")

print(f"What is the answer to this? 89*93")
num1 = int(input(f"Please answer"))
if (num1 != 8277):
   print(f"{num1} is  mistake.")
else:
   print(f"{num1} is correct!")

#challenge 5
num1 = int(input(f"How old are you?"))
if (16 <= num1):
   print(f"You can drive a car!")
else:
   print(f"You're too young to drive!")
