from importar import Carro


adicionar = 1
carros = []

while adicionar != 0:
    modelo = input ("Modelo:")
    cor = input ("Cor:")
    ano = input ("Ano:")
    cr = Carro (modelo,cor,ano)
    carros.append(cr)
    adicionar= int(input("Digite 1 para cadastrar ou 0 para sair"))

else:
    print(f"Você encerrou o aplicativo. \n Segue dados inseridos:")
    for x in carros:
        print(f"Modelo {x.modelo},Cor {x.cor},Ano {x.ano}")

