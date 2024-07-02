def is_even(num: int) -> bool:
    return num % 2 == 0

def main():
    print('Enter 2 numbers to check:')
    a = int(input("First number: "))
    b = int(input("Second number: "))

    if any([is_even(num) for num in [a,b]]):
        print('at least one of the two numbers is even')
    else:
        print('none of those two numbers are even')

if __name__ == '__main__':
    main()