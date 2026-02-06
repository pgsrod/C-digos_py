# exercicio
# desenvolver um programa que guarde os dados de 5 pessoas que estão se candidatando a uma vaga de emprego, sabendo que candidatos menores de 18 anos não podem participar.
# Os dados coletados sao: nome, data de nascimento, telefone, e-mail, formação academica

# modulo/biblioteca para trabalhar com datas
#  usar "import" você pega o modulo inteiro
# para pegar só uma parte dele use: "from 'modulo' import 'coisa'"

from datetime import datetime

candidatos = []

# len-> tamanho (comprimento) da lista

while len(candidatos) < 2:
    # strip -> remove espaço em branco
    # do inicio e do final
    nome = input('Nome Completo: ').strip()
    # isso é para forçar a ter algo escrito. Não pode ser menor que 3 letras
    while len(nome) < 3:
        nome = input('Nome Completo: ').strip()

    data_nasc = input('Data de Nascimento (dd/mm/aaaa): ')
    
    try:
        # converter em um objeto tipo data
        data_convertida = datetime.strptime(data_nasc, "%d/%m/%Y")

    # restrição do problema
        hoje = datetime.now()
    # fazer a conta
        idade = hoje.year - data_convertida.year - \
            ((hoje.month, hoje.day) < (data_convertida.month, data_convertida.day))

        if idade < 18:
            print(f'Candidato tem {idade} anos. Cadastro não permitido')
            continue

    except ValueError:
        print('Data inválida')
        continue

    Telefone = input('telefone: ').strip()
    Email = input('E-mail: ').strip()
    formacao = input('Formação acadêmica: ').strip()

    pessoa = {
        'nome': nome,
        'data_nasc': data_convertida,
        'telefone': Telefone,
        'email': Email,
        'formacao': formacao
    }
    # guardar a pessoa na lista de candidatos
    candidatos.append(pessoa)

print (40*'=')
for candidato in candidatos:
    for chave, valor in candidatos:
        print(f'{chave}: {valor}')
        print(40*'-')