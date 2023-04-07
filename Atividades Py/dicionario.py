dicionario = {"Maria":[31,22,30], "Tito": 26, "Carla":56}
# quadrado = {}

# for itens,value in dicionario.items():
#     quadrado[itens] = value **2
#     print(quadrado)

# acessar posição de item 
posicao = dicionario["Maria"][0]
print(f'O valor do primeiro item da Maria é {posicao}')
   
    
# Automaticamnete o for traz o nome, criamos mais uma variave para percorrer o 
# o valor para retornar o seu quadrado 


d2 = {'João':11,'Pedro':12,'Maria':50,'Sara':40}
for nome in d2.items():
    print(nome)
    #print(f'{nome} tem {idade} anos ')


print(d2['Pedro'])

print(f'Imprimindo usando keys: {dicionario.items()}')

# Por que somente Carla esta sendo printado ?
# Porque eu estava criando outro dicionario ao invés de criar um for
# ou usar a função .key() para ler as chaves ou simplesmente um print

# Para imprimir valores do dicionario usamos o .values

#Para imprimir cada chave com seu valor .items
