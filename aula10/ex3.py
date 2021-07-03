"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "seu nome é curto"; se tiver entre 5 e 6 "seu nome é normal";
mais de 6 "seu nome é muito grande"
"""

x=1
while x!=0:
    #Entra no try caso não haja erro
    try:
        nome=input('Digite o seu primeiro nome? ')

        if len(nome) >0 and len(nome) <= 4:
            print('Seu nome é pequeno!')
            x-=1
        elif len(nome)==5 or len(nome)==6:
            print('Seu nome é normal!')
            x-=1
        elif len(nome)>6:
            print("Seu nome é muito grande!")
            x-=1
        # Entra no else e repete o codigo caso o usuario de enter sem digitar
        else:
            print("Digite um nome.")
    #Entra no except caso ocorra um erro inesperado
    except:
        print('Nome invalido!')