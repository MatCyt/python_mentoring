
def is_right_triangle(sides: list) -> bool:
    sides.sort()
    return sides[0]**2 + sides[1]**2 == sides[2]**2


def main():
    # prompt user to provide length of triangle sides
    print('Enter the lengths of three triangle sides:')
    a = float(input("Length of side A: "))
    b = float(input("Length of side B: "))
    c = float(input("Length of side C: "))

    # check if sides form a right triangle
    if is_right_triangle([a,b,c]):
        print("Provided lenghts form a right triangle")
    else:
        print("Provided lenghts does not form a right triangle")


if __name__ == "__main__":
    main()
    