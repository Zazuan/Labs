string = 'Дана строка, состоящая из слов, пробелов и знаков препинания.'
string = string.split(' ')
for i in range(0, len(string)):
    if sum(c != ' ' for c in string[i]) > 5:
        print(string[i])
