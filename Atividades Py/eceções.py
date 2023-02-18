num= 0
while num != 5:
     try:
        num= int(input(f"Digite: \n 1 Para somar. \n 2 Para subitrair. \n 3 Para multiplicar. \n 4 Para dividir.\n 5 Para sair \n Escolha:"))
        if num == 1:
         num1= int(input("Digite os número:"))
         num2= int(input("Digite os número:"))
         resultado= num1 + num2
         print(f" Soma: {num1} + {num2} = {resultado}")
     
     
        
        elif num == 2:
    
         num1= int(input("Digite os número:"))
         num2= int(input("Digite os número:"))
         resultado= num1 - num2
         print(f" Subtração: {num1} - {num2} = {resultado}")
     

        elif num == 3:
    
         num1= int(input("Digite os número:"))
         num2= int(input("Digite os número:"))
         resultado= num1 * num2
         print(f" Multiplicação : {num1} * {num2} = {resultado}")
     

        else:
    
         num1= int(input("Digite os número:"))
         num2= int(input("Digite os número:"))
         resultado= num1 / num2
         print(f" Divisão: {num1} / {num2} = {resultado}")

     except:
         print("Digite um NÚMERO válido")