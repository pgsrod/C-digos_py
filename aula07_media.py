def media (nota1, nota2):
    media = ('nota1 = nota2')/2

    if media >=7:
        return 'Aprovado'
    
    return 'reprovado'

def verificar_nota():
    nota = float(input('Digite a nota: '))
    while nota < 0 or nota > 10:
        print('Valor inválido. Digite novamente')
        nota = float(input('Digite a nota: '))

    return nota
    
resultado = media(verificar_nota(), verificar_nota())

print(resultado)