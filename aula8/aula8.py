"""
*Criar variáveis para nome(str), idade(int), altura(float) e peso(float) de uma pessoa
*Criar variável com o ano atual(int)
*Obter o ano de nascimento de uma pessoa(baseado na idade e no ano atual)
*Obter o IMC de uma pessoa com 2 casas decimais
*Exibir o texto com valores usando F-Strings
"""
import datetime

nome='Paulo'
idade=23
altura=1.8
peso=78.5
ano=datetime.date.today().year

nascidoEm=ano-idade
imc=peso/altura**2
print(f'{nome} nascido em {nascidoEm} tem {idade} anos, {altura} de altura, {peso}kg e um IMC de {imc:.2f}.'
      f'\n Dados de {ano}')