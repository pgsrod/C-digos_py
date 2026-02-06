print ("jokenpô")
print ("vamos começar!")

print ("1-Pedra")
print ("2-Papel")
print ("3-Tesoura")

jogador1 = int(input("Jogador1: escolha uma opção: "))
jogador2 = int(input("jogador2: escolha uma opção: "))

if jogador1 == jogador2:
    print("empate")

elif jogador1 == 1 and jogador2 == 3:
    print("jogador 1 venceu")

elif jogador1 == 2 and jogador2 == 1:
    print("JOGADOR1 VENCEU")

elif jogador1 == 3 and jogador2 == 2:
    print ("jogador 1 venceu")

else:
    print ("jogador 2 venceu")

# jokenpo versao professor/explicado

pedra = 'Pedra'
papel = 'Papel'
tesoura = 'tesoura'

jogador1 = input ('Faça a sua jogada: ')
jogador2 = input ('Faça a sua jogada: ')

if jogador1 == tesoura:
    if jogador2 == tesoura:
       print ('Empate')
    elif jogador2 == pedra:
       print ('jogador 2 ganhou')
    elif jogador2 == papel:
        print ('jogador 1 ganhou') 

elif jogador1 == papel:
    if jogador2 == papel:
       print ('Empate')
    elif jogador2 == pedra:
       print ('jogador 1 ganhou')
    elif jogador2 == tesoura:
        print ('jogador 2 ganhou') 

elif jogador1 == pedra:
    if jogador2 == pedra:
       print ('Empate')
    elif jogador2 == papel:
       print ('jogador 2 ganhou')
    elif jogador2 == tesoura:
        print ('jogador 1 ganhou')    



