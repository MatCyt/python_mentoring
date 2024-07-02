# simple rock paper

def get_user_choice(user_number: int) -> str:
    user_choice = input(f'User Number {user_number}, select rock, paper or scissors: ')
    if user_choice not in ['rock', 'paper', 'scissors']:
        print('Incorrect value provided!')
        exit()
    return user_choice

def select_winner(val1:str, val2:str) -> None:
    if val1 == val2:
        print("it's a tie!")
    elif (val1 == 'rock' and val2 == 'scissors') or (val1 == 'paper' and val2 == 'rock') or (val1 == 'scissors' and val2 == 'paper'):
        print('user 1 wins!')
    else:
        print('user 2 wins!')

def main():
    user1_choice = get_user_choice(1)
    user2_choice = get_user_choice(2)
    select_winner(user1_choice, user2_choice)

if __name__ == '__main__':
    main()