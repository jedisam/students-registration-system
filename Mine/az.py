def main():
    fibonacciSeries(20)


def fibonacciSeries(endNumber):
    if endNumber <= 0:
        return 'what are u trying to do?'
    elif endNumber == 1:
        return 1
    else:
        x = [1, 1]
        for i in range(2, endNumber):
            num = x[i-2] + x[i-1]
            x.insert(i, num)
        else:
            print('error')

        for num in x:
            print(num, end=' ')


main()
