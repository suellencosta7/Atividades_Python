class Pessoa:
    def __init__(self,nome,idade,estado_civil,):
        self.nome = nome
        self.idade = idade
        self.estado_civil = estado_civil
        

    def Andar (self):
        return 'Eu posso andar!'
    
    def Falar (self):
        return 'Também posso falar!!'
    
ps1 = Pessoa ('João',34,'Casado')
ps1.Andar()
ps1.Falar()      # Para printar o método, chamer com print
print(vars(ps1)) # O método vars retorna todas as informações de um objeto 

class Cliente (Pessoa):
    def __init__(self, nome, idade, estado_civil,comprar):
        super().__init__(nome, idade, estado_civil) # chamar o construtor da superclasse Pessoa
        self.comprar = comprar # Inserindo mais um atributo a Cliente 
    
cl1 = Cliente ('Pedro', 31 , 'Solteiro','Carro')
cl1.Andar()
cl1.Falar()
print(vars(cl1))
print(cl1.Andar() , cl1.Falar())