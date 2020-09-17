import random


def fill_random(a: list, n):
    for i in range(n):
        a.append(random.randint(0, 100))


def print_list(a):
    for element in a:
        print(element, end=' ')
    print()


def sum_list(a):
    summa = 0
    for element in a:
        summa += element
    return summa


def conteyns(a, x):
    for element in a:
        if element == x:
            return True
    return False


def count_chet(a):
    count = 0
    for element in a:
        if element % 2 == 0:
            count += 1
    return count

def chan_list(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] = a[i] // 2


def main():
    n = int(input())
    a = []
    fill_random(a, n)
    print_list(a)
    s = sum_list(a)
    print(s)
    x = int(input())
    v = conteyns(a, x)
    if v == True:
        print('Yes')
    else:
        print('No')
    count = count_chet(a)
    print(count)
    chan_list(a)
    print_list(a)


main()
