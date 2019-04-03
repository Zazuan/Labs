import os

print('Выход из программы: 0')
ans = input('Выберите функцию: 1-4: ')



def cont():
    k = input('Вы хотите продолжить?')
    if k == 'Да' or k == 'yes' or k == 'Y' or k == '1':
        if ans == '1':
            score()
        elif ans == '2':
            #interface()
            print('2')
        elif ans == '3':
            #savefile()
            print('3')
        elif ans == '4':
            exit('Последняя функция')
    elif k == 'Нет' or k == 'no' or k == 'N' or k == '0':
        exit('Завершение работы')


def find():
    path = input('Введите директорию: ')
    count = str(len(next(os.walk(path))))
    print(count)


def score():
    file = open('/Users/zazok/Documents/2 Семестр/ТЯП/textfile.txt', 'r')
    sort = []
    for line in file:
        line = line.strip()
        line = line.split(";")
        sort.append(line)
    new_sort = sort
	for j in range(0, len(new_sort)):
		for i in range(0, len(new_sort)-1):
			if int(new_sort[i][3]) > int(new_sort[i+1][3]):
				stroka = new_sort[i]
				new_sort[i] = new_sort[i+1]
				new_sort[i+1] = stroka
	return new_sort

#def interface():

#def savefile():

if ans == '0':
    exit()

if ans == '1':
    find()
    cont()

elif ans == '2':
    score()
    cont()

elif ans == '3':
#    interface()
    cont()

elif ans == '4':
#    savefile()
    cont()

else:
    print('Введите правильное значение')
