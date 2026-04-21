# Задание 3. Суперпозиция отношений R3 = R1 ◦ R2

def composition_of_relations(R1, R2):
    """
    Параметры:
    R1 - булева матрица отношения R1 на множествах A и B
    R2 - булева матрица отношения R2 на множествах B и C
    Результат:
    R3 - булева матрица суперпозиции отношений R1 и R2 на множествах A и C
    """
    n1 = len(R1)
    m1 = len(R1[0])
    n2 = len(R2)
    m2 = len(R2[0])
    assert(m1 == n2)

    R3 = [[0 for _ in range(m2)] for _ in range(n1)]
    
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                if R1[i][k] == 1 and R2[k][j] == 1:
                    R3[i][j] = 1
                    break
    
    return R3


def convert_relation_to_bin(R_list, A, B):
    """
    Преобразует отношение из списка пар в булеву матрицу
    """
    n = len(A)
    m = len(B)
    R = [[0 for _ in range(m)] for _ in range(n)]
    for pair in R_list:
        ind1 = A.index(pair[0])
        ind2 = B.index(pair[1])
        R[ind1][ind2] = 1
    return R
    

def print_relation(R, name="R"):
    print(f"{name}:")
    for row in R:
        print(list(map(int, row)))


# Данные
A = ["Иванов", "Петров", "Сидоров", "Петечкин", "Васечкин"]  # студенты
B = ["Голодная", "Солодухин", "Рогулин"]                      # преподаватели
C = [1443, 1444, 1447, 1503]                                  # аудитории

# Отношения
R1_list = [("Иванов", "Солодухин"), ("Петечкин", "Рогулин"), ("Сидоров", "Рогулин"), ("Васечкин", "Голодная")]
R2_list = [("Голодная", 1443), ("Солодухин", 1443), ("Солодухин", 1447), ("Рогулин", 1503)]

# Преобразуем в матрицы
R1 = convert_relation_to_bin(R1_list, A, B)
R2 = convert_relation_to_bin(R2_list, B, C)

# Композиция
R3 = composition_of_relations(R1, R2)

# Вывод
print("A =", A)
print("B =", B)
print("C =", C)
print()
print_relation(R1, "R1 (студент → преподаватель)")
print_relation(R2, "R2 (преподаватель → аудитория)")
print_relation(R3, "R3 = R1 ◦ R2 (студент → аудитория)")

# Вывод в виде пар
print("\nРезультат (студент, аудитория):")
for i in range(len(A)):
    for j in range(len(C)):
        if R3[i][j]:
            print(f"({A[i]}, {C[j]})", end="; ")
print()
