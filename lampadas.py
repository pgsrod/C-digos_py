# variaveis: potencia, largura, comprimento, numerolampadas

# a cada m² precisa de 3w 
# a cada 3m² tem um bocal

import math

potencia = int(input('digite a potencia da lampada em watts: '))
largura = float(input('digite a largura do comodo (em metros): '))
comprimento = float(input('digite o comprimento do comodo (em metros): '))

# etapa do calculos
# saber quantos metros quadrados tem no comodo

area = largura * comprimento
numerolampadas = area * 3

# saber quantos watts necessito
potencia_necessaria = area * 3

# saber quantas lampadas é preciso para chegar a potencia necessaria

numero_lampadas= math.ceil(potencia_necessaria/potencia)

# calcular o numero de bocais disponíveis 

numero_bocais = int(area/3)

print(10*'-')
print(f'area do comodo: {area:.2f}m²')
print(f'potencia necessaria: {potencia_necessaria}')
print(f'numero de lampadas: {numero_lampadas}')
print(f'numero de bocais: {numero_bocais}')

if numero_lampadas > numero_bocais:
    print('numero de bocais insuficiente')

