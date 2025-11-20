# PASSWORD GUESSING GAME:
import random
easy_level = ["apple", "banana","cherry", "grapes"]
medium_level = ["biryani","pasta","sandwich","burger"]
hard_level = ["zaid381","zaid2009","zaid@236","muhammad.py"]

print("Welcome to the Password Guessing Game!")
print ("choose a difficulty level: (easy , medium , hard)")

level = input("enter a difficulty level: ").lower()

if level == "easy":
    secret = random.choice(easy_level)
elif level == "medium":
    secret = random.choice(medium_level)
elif level == "hard":
    secret = random.choice(hard_level)
else:
    print("Invalid input....")
    secret = random.choice(medium_level)

attempts = 0
print("\n guess the password:")
while True:
    guess  = input ("enter your guess: ")
    attempts += 1
    if guess == secret:
        print(f"congratulations! you guessed the password '{secret}' in {attempts} attempts.")
        break
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    print("Hint:", hint)
    print(f"game over. the secret password was '{secret}'.")


