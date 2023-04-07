class Veiculo:
    def __init__(self, cor, modelo, ano, estado = False):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano
        self.estado = estado

    def Ligar (self):                      # "self como parametro" representa a instância da classe
     self.estado = True                    # O self permite acessar e manipular os atributos da instância.
      
    def Desligar (self):
     self.estado = True  

class Carro (Veiculo):
   def __init__(self, cor, modelo, ano, estado=False):  # Método construtor Carro
      super().__init__(cor, modelo, ano, estado)        # Método    ||  Classe Veiculo

   def Abrir_Porta(self,porta= True):
      self.porta = porta


class Moto (Veiculo):
   def __init__(self, cor, modelo, ano, estado=False,garupa=False):
      super().__init__(cor, modelo, ano, estado)
      self.garupa = garupa

   def Garupa (self): 
    """ 
    MÉTODO RETONA SE TEM GARUPA.ERRO AO CHAMAR

    """
    self.garupa = True


c1 = Carro ('Preto','Palho',2000)
c1.Ligar()
print(f'O carro está ligado? {c1.estado}')
c1.Desligar
print(f'O carro está Desligado? {c1.estado}')

m1 = Moto ('Branca','Twister',2020)
m1.Ligar()
#help(m1.Ligar)
m1.Garupa()
print(f'Tem garupeiro? {m1.garupa}')
print(f'A moto está ligada?{m1.estado}')


       
