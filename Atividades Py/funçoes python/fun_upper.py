# texto = 'EsTe É um teXto sEM foRMataçÃO'

def tratar_texto (texto):
    texto = texto.upper()
    print(texto)

#tratar_texto(f'Depois:{texto}')

# texto = ['dadOS', 'orGanizaDOS', 'Teste "upper"']

# def tratar_texto (texto):
#     for tex in enumerate(texto):
#         texto = texto.upper()
#     print(texto)

# tratar_texto(f'Depois:{texto}')

texto = ['dadOS', 'orGanizaDOS', 'Teste "upper"']
for posicao, texto_tratado in enumerate(texto):
    texto[posicao] = tratar_texto (texto_tratado) # Passagem de função como tratamento 