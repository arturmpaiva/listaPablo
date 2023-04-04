num = int(input('digite um número maior que 1: '))
cont = 0
listNumerica = []
while (cont <= num):
    listNumerica.append(cont)
    cont += 1
print(sum(listNumerica))