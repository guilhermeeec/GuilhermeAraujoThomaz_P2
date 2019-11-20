def inversao (matriz):  #A
    det = matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
    if det == 0:
        return None
    else:
        inversa =[]
        for linha in range (len(matriz)):
            inversa.append([])
            for coluna in range (len(matriz[0])):
                inversa[linha].append(0)
        inversa[0][0] = matriz[1][1]/det
        inversa[0][1] = (-matriz[0][1])/det
        inversa[1][0] = (-matriz[1][0])/det
        inversa[1][1] = matriz[0][0]/det
        return inversa

def main ():
    a = float(input('Digite o valor de (0,0): '))
    b = float(input('Digite o valor de (0,1): '))
    c = float(input('Digite o valor de (1,0): '))
    d = float(input('Digite o valor de (1,1): '))
    matriz = []
    for linha in range (2):
        matriz.append([])
        for coluna in range (2):
            matriz[linha].append(0)
    matriz[0][0] = a
    matriz[0][1] = b
    matriz[1][0] = c
    matriz[1][1] = d
    inversa = inversao(matriz)
    print('Antes:')
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna], end = '\t')
        print()
    print('Depois:')
    for linha in range(len(inversa)):
        for coluna in range(len(inversa[linha])):
            print(inversa[linha][coluna], end = '\t')
        print()

main()
    
    
    
