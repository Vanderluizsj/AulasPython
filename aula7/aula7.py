"""
Intro Strings
"""
nome = 'Joao'
peso = 90.5
altura = 1.7

print('O IMC de', nome, 'é:', peso/altura**2)  #modo tradicional
print(f'O IMC de {nome} é: {peso/altura**2:.2f}') #com fStrings
imc=peso/altura**2
print('O IMC de {} é: {:.2f}'.format(nome, imc)) #usando função format
#:.2f arredonda para 2 casas

print('O IMC de {1} é: {0}'.format(nome, imc)) #usando indices para indicar ordem