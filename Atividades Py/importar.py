import math # Mais usada 
# from math import *
# from math import pow,log



class Carro:
    def __init__(self, modelo, cor, ano, combustivel):
     
        self.modelo = modelo
        self.cor = cor 
        self.ano = ano
        self.combustivel = combustivel




    def Abastecer (self): # Definindo metodos ao objeto, a cada metodo chamamos uma função
        self.combustivel += 20 # A variavel deve ser inserida na classe anteriormente

        

class Casa:
    def __init__ (self, comodos, moradores):
        self.comodos= comodos 
        self.moradores = moradores


print(math.pow(5,2))    # Boa pratica, inserir o nome da biblioteca com metodo 


