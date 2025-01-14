import random 

print('Welcome to Bagels!')
print('I am thinking of a 3-digit number. Try to guess what it is')
print("""Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.""")

NUMBER_OF_GUESSES = 10
# Generate a random 3-digit number
NUMBER = str(random.randint(100, 999))
print("NUMBER = "+ NUMBER)
print('I have thought of a random number\nYou have 10 guesses to guess it')
print('Time to guess')

while NUMBER_OF_GUESSES > 0:
    guess = str(input('Guess a number: '))
    if len(guess) > 3 or len(guess) < 3:
        print('Please enter a 3-digit number')
        continue
    
    if guess == NUMBER:
        break

    for i in range(len(guess)):
        if guess[i] == NUMBER[i]:
            print('Fermi')
        elif guess[i] in NUMBER:
            print('Pico')
        elif guess[i] not in NUMBER:
            print('Bagels')
    NUMBER_OF_GUESSES -= 1

if guess == NUMBER:
    print('Congratulations! You guessed the number correctly')
elif NUMBER_OF_GUESSES <= 0:
    print('Sorry, you ran out of guesses. The number was'+ NUMBER)
else:
    print('Random error')
            
