
import math
i = True

memoria = [
    (1, 100),
    (2, 250),
    (3, 50),
    (4, 300),
    (5, 150)
]

def First_fit(t):
    for i in memoria:
        print(i[1])
        if i[1] >= t:
            novo = i[0]
            print(novo)
            return novo
    print("memoria indisponivel")
    return None

def Best_fit(t):
    tan = math.inf
    for i in memoria:
        if t <= i[1] and tan > i[1]:
            novo = i[0]
            print(novo)
            tan = i[1]
            print(tan)
    return novo

def Worst_fit(t):
    tan = -math.inf
    for i in memoria:
        if t <= i[1] and tan < i[1]:
            novo = i[0]
            print(novo)
            tan = i[1]
            print(tan)
    return novo
while True:
    nova_m = None
    print("Escolha o algoritmo de alocação:")
    print("1. First-fit")
    print("2. Best-fit")
    print("3. Worst-fit")
    print("4. Sair")
    ver = int(input())

    if ver == 4:
        break

    b = int(input("informe o tamanho do arquivo"))

    if ver == 1:
        novo_m = First_fit(b)
    elif ver == 2:
        novo_m = Best_fit(b)
    else:
        novo_m = Worst_fit(b)

    if novo_m is not None:
        memoria[novo_m - 1] = (novo_m, memoria[novo_m - 1][1] - b)
    else:
        print("memoria indisponivel")

    print(memoria)