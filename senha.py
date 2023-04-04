senha = 'futebol'
cont = 1
if (cont != 3):
    chute = input("Digite a senha: ")

while cont < 3:

    cont += 1
    if chute == 'futebol':
        print('Bem-vindo!')
        break
    else:
       chute = input('Tente novamente: ')

if cont == 3:
    print("Tentativas excedidas!")