#variaveis ( boas praticas)
# Nao pode:
# 1. iniciar com numero
# 2. tente nao comecar com caracteres especiais
# _ab = 1

# ideal -> comecar com letra minuscula
# ideal -> usar uma so formatacao
# Obs.: Tudo maiusculo indica uma "constante"

# formatacao
# 1. snake_case: underline no lugar do spaco
# ex.:
rio_de_janeiro = 'cuidado'

# camelCase: onde teria o espaco, letra maiuscula
rioDeJaneiro  = 'cuidado redobrado'

# 3; PascalCase: usado para classes (sempre inicia a palavra com letra maiuscula)
RioDejaneiro = 'a'



# etapa 1: pegar as notas (4)
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
nota4 = float(input('digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4

print('Média do aluno(a): ', media)

# print('Média do aluno(a): ', media)

if media > 7:
    print('aprovado')

elif media >= 5 and media <=7:
    print('em recuperacao')

else:
    print('reprovado')

# exercicio finalizado

