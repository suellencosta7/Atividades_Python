# Escreva um programa que leia um dicionário contendo o nome e a idade de várias
# pessoas e exiba o nome da pessoa mais velha.

person ={'João':35,'Pedro':27,'Diana':55,'Denis':37,'Paulo':58,'Sara':39}
pessoa = max(person, key=person.get)
# older = max(person.values())
print(f'O mais velho é o {pessoa} ')

# Escreva um programa que leia um dicionário contendo o nome e o preço de
# vários produtos e exiba o nome e o preço do produto mais caro.

loja = {'Camiseta':30.00,'Jeans':110.00,'Short':65.90,'Blusa social':85.00}

more_product = max(loja, key=loja.get)
value = max(loja.values())

print(f'O produto mais caro é {more_product} no valor de {value}')


# Escreva uma função que recebe um dicionário contendo
#  o nome e a altura de várias pessoas e retorna o nome da pessoa mais alta.

info_person = {'Diana': 1.5, 'Joana':1.70, 'Denix':1.75, 'Rosana':1.90}
taller_person = max(info_person, key=info_person.get)
hight = max(info_person.values())

print(f'A pessoa mais alta é {taller_person}')

def taller (dicionario):
    person = max(dicionario, key=dicionario.get)
    print(person) 

taller(info_person)

# for nome,older in person.items():
#    print(f'{nome} tem {older} anos.')
#
