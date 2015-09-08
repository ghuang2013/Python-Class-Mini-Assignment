# COT 4930  Python Programming
# name: Guan Huang
# id  : Z23265757
# lab : 03


def eratos(n):
    prime_list = [each_prime for each_prime in range(2, n + 1)]
    for key_index, divisor in enumerate(prime_list):
        next_index = key_index + 1
        while next_index < len(prime_list):
            if prime_list[next_index] % divisor == 0:
                prime_list.remove(prime_list[next_index])
            else:
                next_index += 1
    return prime_list


def print_primes(primes):
    for index, prime in enumerate(primes):
        print("{:5d}".format(prime), end='')
        if (index + 1) % 10 == 0:
            print()


def main():
    try:
        range = int(input("Please enter a range for prime calculation >= 2 and <= 300: "))
        if range < 2 or range > 300:
            raise RuntimeError("illegal range")
        prime_list = eratos(range)
        print_primes(prime_list)
    except ValueError as e:
        print("Conversion error:", e.__str__())
    except RuntimeError as e:
        print("Runtime error:", e.__str__())


if __name__ == "__main__":
    main()
