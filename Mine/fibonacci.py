def main():
    num = int(input('Enter the limit of fibbonacci u wanna ..'))
    fibonacci_generator(num)


def fibonacci_generator(num):
    a = 1
    b = 1
    while b <= num:
        print(a, b, end=' ')
        a = a + b
        b = b + a


if __name__ == '__main__':
    main()

# 1 1 2 3 5 8 13
