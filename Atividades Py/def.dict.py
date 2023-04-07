# Escreva uma função que recebe uma lista de dicionários contendo informações
# sobre vários produtos e retorna uma nova lista contendo apenas os produtos com 
# preço maior que R$100.


products = {'Notbook': 3500.00,'Tablet':250.00, 'Mouser':50.00, 'Estojo escolar':25.00}
new_produts = []
def more_hunder (prodts):
    for expensive in prodts.values():
        if expensive > 100:
            new_produts.append(expensive)
    print(new_produts)



more_hunder(products)
