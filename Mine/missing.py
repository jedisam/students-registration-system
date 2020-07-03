def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    missing(arr)


def missing(arr):
    for i in range(1, 11):
        found = False
        for k in arr:
            if k == i:
                found = True
                break
        if found == False:
            print(f'There is missing number: {i}')
            break
    else:
        print('No Missing number!')


main()
