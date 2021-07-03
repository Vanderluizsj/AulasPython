import datetime
nome=input("Qual seu nome? ")
print(f'O usuario digitou {nome} e o tipo da variável é' f'{type(nome)}')

idade=input('Qual sua idade? ')
anoAtual=datetime.date.today().year
anoNascimento=anoAtual-int(idade)

print(f'{nome} tem {idade} anos de idade e '
      f'nasceu em {anoNascimento}')