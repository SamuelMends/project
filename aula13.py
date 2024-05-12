nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
print('Seu IMC é de {:.2f}'.format(imc))

# f-strings
linha_1 = f'Nome de {nome} \npossui a altura de {altura} \ne o peso de {peso} '

print(linha_1)