def get_highest_value(values: list) -> int:
    values.sort()
    highest = values[-1]
    return highest

def main():
    print('Enter 3 numbers to compare:')
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))

    highest_number = get_highest_value([a,b,c])

    print(f'Highest number is {highest_number}')

if __name__ == '__main__':
    main()
