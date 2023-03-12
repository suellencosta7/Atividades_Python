class Pessoa: # Ciar classe
    def __init__ (self, nome, idade, sexo,falar,andar): # Definindo atributos
        self.nome = nome # Tornando os parametros acessiveis 
        self.idade = idade 
        self.sexo = sexo
        self.falar = falar 
        self.andar = andar
        
    def Andar (self):
        if self.andar == True:
          print("Posso andar")
        else: 
          print ("Não posso andar")

    def Falar (self):
       if self.falar == True:
          print("Posso falar")
       else: 
          print ("Não posso falar")


#person = Pessoa ("Maria",25,"Femenino") # Instansiando a classe e declarando os valore
#print (person.sexo) # Acessar 


class Bens:
    def __init__  (self, carro, casa, propriedades):
      self.carro = carro
      self.casa = casa
      self.propriedades = propriedades