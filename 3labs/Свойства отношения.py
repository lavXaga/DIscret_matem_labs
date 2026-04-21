# Задание 1. Проверка свойств отношения (рефлексивность, симметричность, транзитивность)

def analyze_relation(R):
    """
    Выясняет свойства отношения, заданного квадратной булевой матрицей R
    """
    n = len(R)
    
    # Рефлексивность
    reflexive = True
    for i in range(n):
        if R[i][i] != 1:
            reflexive = False
            break
    
    # Симметричность
    symmetric = True
    for i in range(n):
        for j in range(n):
            if R[i][j] != R[j][i]:
                symmetric = False
                break
        if not symmetric:
            break
    
    # Транзитивность
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

   
def print_relation(R):
    for row in R:
        print(list(map(int, row)))


# Пример 1
A1 = ["Иванов", "Петров", "Сидоров", "Петечкин", "Васечкин"]
n1 = len(A1)

R1 = [[0 for _ in range(n1)] for _ in range(n1)]
R1_list = [("Иванов", "Петров"), ("Петров", "Сидоров"), ("Иванов", "Петечкин")]

for p in R1_list:
    ind1 = A1.index(p[0])
    ind2 = A1.index(p[1])
    R1[ind1][ind2] = 1

print("R1:")
print_relation(R1)
analyze_relation(R1)

# Пример 2
A2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n2 = len(A2)

def F2(x, y):
    return (x < y)

R2 = [[F2(A2[i], A2[j]) for j in range(n2)] for i in range(n2)]
print("\nR2 (x < y):")
print_relation(R2)
analyze_relation(R2)

# Пример 3
A3 = A2
n3 = len(A3)

def F3(x, y):
    return (x + y) % 2 == 0

R3 = [[F3(A3[i], A3[j]) for j in range(n3)] for i in range(n3)]
print("\nR3 (x + y четное):")
print_relation(R3)
analyze_relation(R3)
