cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
num = int
while(num != 0):
    num = int(input("Digite um número de 1 a 100: "))
    if(1 <= num and num <= 25):
        cont1 += 1
    elif (26 <= num and num <= 50):
        cont2 += 1
    elif (51 <= num and num <= 75):
        cont3 += 1
    elif (76 <= num and num <= 100):
        cont4 += 1
    else:
        print("Número fora do intervalo!")
print("Existem {} números no intervalo [1-25]".format(cont1))
print("Existem {} números no intervalo [26-50]".format(cont2))
print("Existem {} números no intervalo [51-75]".format(cont3))
print("Existem {} números no intervalo [76-100]".format(cont4))