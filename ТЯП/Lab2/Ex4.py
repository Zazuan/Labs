k = int(input('Количество элементов: '))

if k < 10:
    print('Количество элементов должно быть больше 10')
    k = int(input('Попробуйте снова: '))

s = []
for i in range(1, k+1):
    s.append(int(input('Введите ' + str(i) + ' элемент списка: ')))
print(s)

for i in range(2):
    del s[slice(0, 1)]
    s.append(int(input('Введите новый элемент: ')))
print(s)
print('Количество элементов: ' + str(len(s)))
