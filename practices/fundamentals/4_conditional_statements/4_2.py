def check_sign(num: int) -> None:
    if num < 0:
        print("Provided number is negative")
    elif num > 0:
        print("Provided number is positive")
    else:
        print("Provided number equals 0")

def main():
    user_input = float(input("Please provide number to be checked: "))
    check_sign(user_input)

if __name__ == "__main__":
    main()