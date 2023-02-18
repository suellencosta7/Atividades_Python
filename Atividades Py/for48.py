# Selecionar os números impares no intervalo definido, e calcular os multiplos de 3

for n in range (1,501):
    if n % 2 != 0:
        f=n
        print(f"Números impares: {f}")
        if f % 3 == 0:
            print(f"Numero impa que é multiplo de 3 {f}")
            s= f+f
            print (f"Soma {s};")
