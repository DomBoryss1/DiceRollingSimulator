import random

def roll_dice():
  roll = random.randint(1, 6)
  return roll

print("Rolling The Dice...")
print("You Rolled A", roll_dice())
