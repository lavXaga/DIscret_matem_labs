# Задание 2. Обратное отношение

def inverse_relation(R):
    """
    Возвращает матрицу обратного отношения R^{-1}
    """
    n = len(R)
    R_inv = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            R_inv[j][i] = R[i][j]
    return R_inv


def print_relation(R, name="R"):
    print(f"{name}:")
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

print_relation(R1, "R1")
R1_inv = inverse_relation(R1)
print_relation(R1_inv, "R1^{-1} (обратное отношение)")


# Пример 2
A2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n2 = len(A2)

def F2(x, y):
    return (x < y)

R2 = [[F2(A2[i], A2[j]) for j in range(n2)] for i in range(n2)]

print("\n")
print_relation(R2, "R2 (x < y)")
R2_inv = inverse_relation(R2)
print_relation(R2_inv, "R2^{-1} (обратное отношение)")


# Пример 3
A3 = A2
n3 = len(A3)

def F3(x, y):
    return (x + y) % 2 == 0

R3 = [[F3(A3[i], A3[j]) for j in range(n3)] for i in range(n3)]

print("\n")
print_relation(R3, "R3 (x + y четное)")
R3_inv = inverse_relation(R3)
print_relation(R3_inv, "R3^{-1} (обратное отношение)")
