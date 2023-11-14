import random

name = input("What is your name? ")
print("Welcome, " + name + "! I'm thinking of a number between 1 and 100.")

my_number = random.randint(1, 100)
guesses = []

for guess_number in range(1, 11):
    valid_guess = False
    while not valid_guess:
        try:
            user_guess = int(input("Take a guess...\n"))
            valid_guess = True
        except ValueError:
            print("Duuude, put in a number.")

    difference = abs(my_number - user_guess)
    guesses.append(user_guess)

    if user_guess < my_number and difference > 10:
        print("Wayyy too low my dude, try again.")
    elif user_guess < my_number:
        print("Lil low my dude, try again.")
    elif user_guess > my_number and difference > 10:
        print("Wayyy too high my dude, try again.")
    elif user_guess > my_number:
        print("Lil high my dude, try again.")
    elif user_guess == my_number:
        print("Noooice " + name + "! You guessed my number in " + str(guess_number) + " guesses.")
        break
else:
    print("You lose, " + name + ". The number I was thinking of was " + str(my_number))

print("Here are your guesses: " + ", ".join(str(x) for x in guesses))
