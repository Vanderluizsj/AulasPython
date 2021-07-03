"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se esse numero é par ou impar. Caso o usuário não digite um numero inteiro,
informe que não é um numero inteiro.
"""

x=1
while x!=0: #repete a solicitação até um numero inteiro ser digitado
    try:
        n1=int(input('Digite um numero inteiro: '))
        if n1%2 == 0:
            print('O numero é par.')
            x-=1
        else:
            print('O numero é impar.')
            x-=1
    except:
        print('O caracter digitado não é um numero inteiro. ')