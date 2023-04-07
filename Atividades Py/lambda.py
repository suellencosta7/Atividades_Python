# Escreva uma função lambda que retorne o quadrado de um número.

nums = [2,4] # Crei uma lita dos quadrados que desejo
quadrado_numero = list (map(lambda x: x ** 2,nums))
# O map precisa de um funçaõ, nete caso é a Lambda, e uma lista, nums

# Função Lambda recebe uma informação e retorna outra, ou seja , recebe nums como argumento
# e map percorre a mesma fazendo o quadrado de cada um
print (quadrado_numero)


# Escreva uma função lambda que retorne True se um número é par e False caso contrário.

num = 5
true_false = lambda x : x % 2 == 0

print(true_false(num))

# Use a função map() para retornar uma lista com os números pares em outra lista.

lista = [3,5,8,10,20,30,7]
lista_par = []

lista_par = list(filter(lambda x: x % 2 == 0,lista))

print(lista_par)


# Use a função map() para converter uma lista de strings em uma lista de inteiros.

str_to_int = ['2','4','6']

converter = list(map(lambda x: int(x)+2, str_to_int))
print(converter)





