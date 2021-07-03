"""
Faça um programa que pergunte a hora aousuário e, baseando-se na hora descrita,
exiba a saudação apropriada.
"""

x=1
while x!=0:
    #Entra no try caso seja digitado um numero inteiro
    try:
        horas=int(input('Que horas são? '))
        if horas>=0 and horas<=11:
            print('Bom dia!')
            x-=1
        elif horas>=12 and horas<=17:
            print('Boa tarde!')
            x-=1
        elif horas>=13 and horas<=23:
            print('Boa noite!')
            x-=1
        #Caso o numero seja superior a 23 ou inferior a 0 entra no else e repete o programa
        else:
            print("Digite uma hora entre 0 e 23.")
    #Entra no except e repete o codigo caso o caracter digitado não seja um numero inteiro
    except:
        print("Digite apenas o numero correspondente a hora.")
