def fill_list(a: list, n):
    for i in range(n):
        if i % 2 == 0:
            a.append(0)
        else:
            a.append(1)


def fill_fibo(a: list, n):
    a.append(0)
    a.append(1)
    for i in range(2, n):
        a.append(a[i - 1] + a[i - 2])


def print_list(a):
    for element in a:
        print(element, end=' ')
    print()


def main():
    n = int(input('Введите кол-во эл-тов: '))
    a = []
    fill_fibo(a, n)
    print_list(a)


main()
