class Pessoa:
    def __init__(self, id) :
        self.__nome = None  # Inicializa o atributo nome como None     
        self.id = id

    def declarar_nome (self,nome): # Método para declarar nome 
        self.__nome = nome
        
    def obter_nome (self):
     return self.__nome
    
    
    def obter_id(self):
     return self.id
     

pessoa1 = Pessoa(2)

pessoa1.declarar_nome('Nina')

print(pessoa1.obter_nome())



        
# Crie uma classe chamada "Pessoa" com um atributo
# privado "nome" (representado como "__nome") e um 
# atributo público "id". Adicione duas funções à classe,
# uma para definir o valor de "nome" e outra para obter o 
# valor de "nome". Observe que o atributo "nome" deve ser 
# privado e acessado somente através dessas funções.


