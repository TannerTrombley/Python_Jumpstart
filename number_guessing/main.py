import random


def run():
    """
    Generates a random number and then promps a user to guess the number until they get it right.
    :return: None
    """
    print('--------------------------')
    print('     Guess the number')
    print('--------------------------')

    generated_num = random.randint(0, 100)
    # Guess has an initial value that cannot be the random
    guess = -1

    while guess != generated_num:
        guess = int(input('Enter a guess: '))

        if guess < generated_num:
            print('{} is too LOW'.format(guess))
        elif guess > generated_num:
            print('{} is too HIGH'.format(guess))
        else:
            print('{} is CORRECT'.format(guess))

    print('Done')


if __name__ == "__main__":
    run()
