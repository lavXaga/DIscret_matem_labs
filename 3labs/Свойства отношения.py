def analyze_relation(R):
    
    n = len(R)
    
    # Проверка рефлексивности: все элементы на главной диагонали должны быть 1
    reflexive = True
    for i in range(n):
        if R[i][i] != 1:
            reflexive = False
            break
    
    # Проверка симметричности: R[i][j] == R[j][i] для всех i, j
    symmetric = True
    for i in range(n):
        for j in range(n):
            if R[i][j] != R[j][i]:
                symmetric = False
                break
        if not symmetric:
            break
    
    # Проверка транзитивности: если R[i][j] == 1 и R[j][k] == 1, то R[i][k] == 1
    transitive = True
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if R[i][j] == 1 and R[j][k] == 1 and R[i][k] != 1:
                    transitive = False
                    break
            if not transitive:
                break
        if not transitive:
            break
    
    print("Рефлексивность:", reflexive)
    print("Симметричность:", symmetric)
    print("Транзитивность:", transitive)
