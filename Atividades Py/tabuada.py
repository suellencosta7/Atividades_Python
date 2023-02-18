def multi (num): # Recebe o número da tabuada que será printada
   for n in range (1,11): # Sequencia que irá multiplicar 
        print(f"{num} X {n} = {num*n}") 

num=int(input("Qual tabuada você deseja visitar:")) # Variavel recebe o produto
multi(num) # Chamada da função 

## OUTRO METODO ##

num1=int(input(f"Qual tabuada deseja visitar:"))
for num in range (1,11):  
      print(f"{num1} X {num} = {num1 * num}")