secretnum = 5
guess = int(input("Guess a number: "))
if guess<secretnum:
    print("Too low")
elif guess>secretnum:
    print("Too high")
else:
    print("Same as the secret!")