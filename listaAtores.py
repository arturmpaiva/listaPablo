#5 atores
#buscar na lista um determinado nome, dizer se tem ou n
#tbm deletar o nome

atores = ['brad', 'leo', 'steve', 'blake', 'sarah']
nome = input("Digite um ator para checar se se encontra na lista")

if nome in atores:
    print(nome, "está na lista")
    del atores[atores.index(nome)]
else :
    print(nome, "não está na lista")
