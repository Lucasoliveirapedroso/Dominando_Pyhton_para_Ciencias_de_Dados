numeros = [0,1,2,3,4,5,6,7,8,9,10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(pares)

#forma 1
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)