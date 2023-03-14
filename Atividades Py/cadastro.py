import classe # referencia de onde a classe esta

#from classe import Pessoa

maria = classe.Pessoa ("Maria", 17,"F",False,6) 
joao = classe.Pessoa ("João",23,"M",True,0)


joao.Falar()
joao.Andar(5)
print(f'{joao.nome} andou {joao.passos} passos')
joao.Andar(15)
print(f'{joao.nome} andou mais alguns passos , ao todo  foram {joao.passos} passos')


""" 
Obs: Para o print se tornar True, é necessário chamar o objeto, joão 
e o que deseja que apareça, nome,idade , "F/M". . .

1° Tentativa , chamei usando apenas a variavel JOÃO, porem ela é um objeto, e precisa 
ser especificado o que gostaria de puxar do obj.

"""

#print()maria.Andar(10)