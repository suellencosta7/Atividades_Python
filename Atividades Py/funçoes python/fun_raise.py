 
def new_person():
    """
    Função que pega do usuário, nome e idade, caso insiram caracteres incorretos em algum input,
    retorna ERRO!
    """
  
    nome = (input('Insira seu nome:'))
    if nome != str:
        raise ValueError('ERRO: Você esta inserindo números ou caracteres não aceitos.')
    idade = (input('Insira sua idade:'))
    if idade != int:
     raise ValueError('ERRO: Você estar inserindo valor diferente ao que se pede')
    
    return  f'Olá, {nome}'
       
    
    



new_person()
#adicionar mensagem de erro 