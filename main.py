# to use a random number
import random
# create the random number
r = random.randint(1, 99)
# create the input number
guess = int(input("Enter an integer from 1 to 99: "))
# start testing by compare the random number (r) with the input number (guess)
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
