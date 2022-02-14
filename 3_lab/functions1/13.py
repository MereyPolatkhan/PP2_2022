def guess():
    name = input('Hello! What is your name?\n')

    number = int(input(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess\n'))
    k = 1
    while True:
        if number >= 19:
            print(f'Good job, KBTU! You guessed my number in {k} guesses!')
            break
        else:
            print('Your guess is too low.\nTake a guess.')
            number = int(input())
            k += 1



guess()     