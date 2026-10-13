secretnum = 5
guess = int(input("Guess a number: "))
while guess!=secretnum:
    if guess<secretnum:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess a number: "))
print("Conguratulations! Same as the secret. ")

