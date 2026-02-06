#





#etapa 1 -> input() -> pega o usuario
#digita

numero1 = int(input('informe um numero: '))
numero2 = int(input('informe um numero: '))
numero3 = int(input('informe um numero: '))

#etapa 2 -> comparar os numeros
maior = numero1
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero3:
    maior = numero2
else:
    maior = numero3

print('o maior numero é: ', maior)