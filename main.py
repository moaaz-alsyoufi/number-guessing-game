import random
r = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))
while True:
  if guess < r:
    print("Your number is lower. Try again")
    guess = int(input("Enter an integer from 1 to 99: "))
  elif guess > r:
    print("Your number is higher. Try again")
    guess = int(input("Enter an integer from 1 to 99: "))
  else:
    print("You guessed it!")
    break
