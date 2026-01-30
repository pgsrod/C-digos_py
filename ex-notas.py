# construa um programa que só aceite notas escolares entre zero e dez
# somente notas entre zero e dez devem ser aceitas

nota = float(input('Digite a nota: '))

while nota < 0 or nota > 10:
    print('Valor inválido, Digite novamente')
    nota = float(input('Digite a nota: '))

print(nota)