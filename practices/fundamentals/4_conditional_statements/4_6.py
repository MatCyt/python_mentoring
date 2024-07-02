
import random
import time

def toss_coin() -> str:
    # random toss result
    result = random.choice(['heads', 'tails'])
    return result

def main():
    user_score = 0
    computer_score = 0
    print('Welcome to heads and tails game. For each correct guess you will receive a point. For incorrect - a computer receives one. \n The game lasts until one side will get 2 points in total')

    while user_score <= 2 and computer_score <= 2:
        user_choice = input('Please select heads or tails:')

        print('tossing in:')
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

        result = toss_coin()
        print(f'toss result: {result}')

        if (user_choice == 'heads' and result == 'heads') or (user_choice == 'tails' and result == 'tails'):
            user_score += 1
            print('that is a correct guess!')
        else:
            computer_score += 1
            print('the computer has won')

        print(f'current result | user: {user_score}, computer: {computer_score}')

    print(f'The game has ended with result:  user: {user_score}, computer: {computer_score}')

if __name__ == '__main__':
    main()