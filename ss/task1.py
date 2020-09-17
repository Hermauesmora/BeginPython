a = [2, 5, 6, 30]
a.pop(2)
a.insert(1, 100)
a.remove(100)

b = 7
if b in a:
    print('Yes')

print(a)
# for element in a:
#     print(element, end=' ')

for i in range(len(a)):
    print(a[i], end=' ')
