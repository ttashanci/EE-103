x = int(input("Enter an int: "))
guess = 0
while guess**3 < abs(x):
    guess += 1
if guess**3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        guess = -guess
    print("Cube root of " + str(x) + " is " + str(guess))