def invite_more_women(arr):
    count_man = 0
    count_women = 0
    for element in arr:
        if element == 1:
            count_man += 1
        else:
            count_women += 1
    if count_women < count_man:
        return True
    else:
        return False


def invite_more_women_2(arr:list):
    count_man = arr.count(1)
    count_women = arr.count(-1)
    if count_women < count_man:
        return True
    else:
        return False


def main():
    a = [1, -1, 1]
    v = invite_more_women(a)
    if v == True:
        print('Приглашаем')
    else:
        print('Не нужно приглашать')


main()
