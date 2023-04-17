class Pessoa :
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade 
    # Criando Metodo, o self como parametro, acessa e manipula os atributos da instância
    def Saudacao (self): 
        print (f'Olá {self.nome} você tem {self.idade} anos')
    
maria = Pessoa('Maria',24)
maria.Saudacao()

   .     