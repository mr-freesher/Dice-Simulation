import random

def roll_dice():
    # Generate a random number between 1 and 6 (inclusive)
    return random.randint(1, 6)

# Simulate rolling the dice 10 times  for loop
# for i in range(10):
#     print("Roll", i+1, ":", roll_dice())

# Simulate rolling the dice 10 times While loop
num = int(input("If you want to simulate enter 1 : "))
while num <=10:
    print("Roll", num, ":", roll_dice())
    num+=1

# Success
