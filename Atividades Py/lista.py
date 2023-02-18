

escolha = 1
listaPessoa = []

while escolha != 0:
    nome = input("Nome:")
    idade = int(input("Idade:"))
    usuario = (nome,idade)
    listaPessoa.append(usuario) 
    escolha = int(input("Digite 1 para continuar ou 0 pra sair."))
   
else:
    print("Você encerrou o programa")
    print(listaPessoa)
    





