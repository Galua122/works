word = 'гп' - задаем слово
a = ['г', 'п'] - создаем алфавит
g = ['****', '*', '*']       - создаем буквы
p = ['****', '*  *', '*  *']

b = [g, p] - создаем матрицу
ch = [a.index(x) for x in list(word)] - находим какой индекс в списке алфавита соотносится с каждой буквой
for i in range(len(b[0])):
    for j in range(len(ch)):
        print(b[ch[j]][i], end=' ')
    print()
