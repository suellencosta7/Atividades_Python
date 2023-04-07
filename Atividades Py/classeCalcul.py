
class Calculo:
    def Subtração (self,x,y) :  # Já retorna como print
       print(x - y)

    def Soma (self,x,y):        #
        return x + y
        
    def Media (self,x,y,z):
        return (x + y + z) / 3  #

opera = Calculo()               # Cria o objeto 'Opera'
opera.Subtração(4,4)    

operacao = Calculo()
vlr = operacao.Media(5,5,5)    # Variavél que armazena o valor da operação

print(vlr)              
