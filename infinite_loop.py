secretnum = 5
attempts = 0
found = False
while attempts < 5:
    guess = int(input("Guess a number: "))
    attempts += 1
    if guess == secretnum:
        print("Congratulations! You guessed the secret number.")
        found = True
        break
    elif guess < secretnum:
        print("Too low!")
    else:
        print("Too high!")
if not found:
    while True:
        print("Oh! Noooo...")