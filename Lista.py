ListaCompleta=[]



for c in range(6):

    num=int(input(f"Digite Seis Números:[{c}]: "))
    ListaCompleta.append(num)
    len(ListaCompleta)
    Par=[numPar for numPar in ListaCompleta if numPar% 2==0]
    Impar=[numImpar for numImpar in ListaCompleta if numImpar% 2!=0]

print(f"A sua Lista Completa é: {ListaCompleta}")
print(f"A Lista de Números Pares é: {Par}")
print(f"A Lista de Números Impares é: {Impar}")

