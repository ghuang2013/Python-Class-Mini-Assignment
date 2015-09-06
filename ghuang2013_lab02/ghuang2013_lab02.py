__author__ = 'ghuan_000'


def fib(n, myList):
    myList.append(0)
    myList.append(1)

    for i in range(2, n):
        myList.append(myList[i - 1] + myList[i - 2])


def main():
    fib_list = list()

    try:
        number_of_term = int(input("Enter number of terms to be generated: "))
        if number_of_term < 2 or number_of_term > 20:
            raise RuntimeError("Please enter an between 2 and 20")

        fib(number_of_term, fib_list)

        for index in range(0, len(fib_list)):
            print("%5d" % fib_list[index], end='')
            if (index + 1) % 6 == 0:
                print()

    except (ValueError, RuntimeError) as exp:
        print("Oh no, something goes wrong: ", exp)


if __name__ == "__main__":
    main()
