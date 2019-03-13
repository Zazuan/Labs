my_string = "Ф;И;О;Возраст;Категория" \
            ";_Иванов;Иван;Иванович;23 года;Студент 3 курса"\
            ";_Петров;Семен;Игоревич;22 года;Студент 2 курса"
my_string = my_string.split(';_')
for i in range(0, len(my_string)):
    string = my_string[i]
    string = string.split(';')
    print(string[0] + ' ' + string[1] + ' ' + string[2] + '     ' + string[3] + '     ' + string[4])
