nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
idade = int(input('Digite sua idade: '))
ano_nascimento = int(input('Ano de nascimento: '))
maioridade = idade >=18
altura_metros = float(input('Digite sua altura em metros: '))

print('-'*30)
print('Nome: {}'.format(nome))
print('Sobrenome: {}'.format(sobrenome))
print('Idade: {}'.format(idade))
print('Ano de nascimento: {}'.format(ano_nascimento))
print('É maior de idade? {}'.format(maioridade))
print('Altura em metros: {}'.format(altura_metros))