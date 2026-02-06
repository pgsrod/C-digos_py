

import random

# 1) gerar dados

def gerar_dados(qtd, minimo, maximo): 
# ''' Gera uma lista com 'qtd' números inteiros pseudo aleatórios '''

    dados = []

# o  "_" (underline) serve para dizer para o python que esse for é apenas para executar o comando várias vezes. 

    for _ in range (qtd):
        dados.append(random.radint(minimo, maximo)) 
    
    return dados

# 2) processar dados -> tente dar nome com 'significado'

def calcular_total (valores):
    return sum(valores)
    # total = 0
    # for valor in valores:
    #     total+=valores 
    #     # total = total+valor
    # return valores

def calcular_media (valores):
    '''Calcula medi dos valores. Retorna 0 se a lista estiver vazia'''
    # if len(valores) == 0:
    #     return 0
# outra forma de fazer: pergunta se tem nada dentro da variavel 
    if not valores:
        return 0 
    total = calcular_total (valores)
    return total/len(valores)   

def calcula_amplitude (valores):
    '''calcula a amplitude dos valores, pegando o máximo e o mínimo da lista '''
    maximo = max(valores)
    minimo = min (valores)

    return maximo - minimo 
# ou return max - min (valores)

def calcular_projecao(valores, fator):
    pass

def exibir_resultados (dados):
    '''Mosta os dados e calculos realizados'''

    print(f'Dados Gerados: {dados}')

    print(f'Soma: {calcular_total(dados)}')

    media = calcular_media(dados)
    print (f'Média: {media}')

    print (f' A amplitutide dos dados é: {calcula_amplitude(dados)}')

def main():
    qtd = 10
    minimo = 0
    maximo = 100

    dados = gerar_dados(qtd, minimo, maximo)

    exibir_resultados(dados)

main()


   