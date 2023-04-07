# Escreva uma função que receba uma lista de números e retorne uma nova lista com os
# valores originais elevados ao quadrado.

# numbers = [2,4,6,8,10,12]

# num_quadrado = list(map(lambda x: x**2,numbers))

# print(num_quadrado)

# Escreva uma função que receba uma lista de nomes em minúsculas e retorne uma nova lista 
# com os nomes capitalizados.

# def nomes_minusculos (list_names):
#     new_names = list(map(lambda x: x.capitalize(), list_names))
#     return new_names

# names = ['marIa','joão','junia']
# print(nomes_minusculos(names))

# Escreva uma função que receba uma lista de dicionários representando pessoas 
# (com chaves 'nome' e 'idade') e retorne uma nova lista com as idades das pessoas.

dicionario = {'Maria':32,'João': 41,'Pedro': 30}
new = {}
get_years =dicionario.values()
#get_y = list(map(lambda x: dicionario[1] , dicionario))

print(get_years)
print(type(get_years))