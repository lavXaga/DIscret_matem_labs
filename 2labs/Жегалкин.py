def f(x, y, z):
    return x or (not y) or z


def truth_table_by_func(f):
    tt = {}
    for x in range(2):
        for y in range(2):
            for z in range(2):
                tt[x, y, z] = int(f(x, y, z))
    return tt


def xor_polynom(tt):
    tt_line = []
    for x in range(2):
        for y in range(2):
            for z in range(2):
                tt_line.append(tt[x, y, z])
    
    triangle = [tt_line[:]]
    current = tt_line[:]
    while len(current) > 1:
        new_line = []
        for i in range(len(current) - 1):
            new_line.append(current[i] ^ current[i + 1])
        triangle.append(new_line)
        current = new_line
    
    print("Треугольник:")
    for line in triangle:
        print(line)
    
    coeffs = [line[0] for line in triangle]
    
    terms = []
    var_masks = [[], [2], [1], [1,2], [0], [0,2], [0,1], [0,1,2]]
    
    for i, c in enumerate(coeffs):
        if c == 1:
            if i == 0:
                terms.append("1")
            else:
                part = []
                if 0 in var_masks[i]: part.append("x")
                if 1 in var_masks[i]: part.append("y")
                if 2 in var_masks[i]: part.append("z")
                terms.append("".join(part))
    
    return " ⊕ ".join(terms) if terms else "0"


if __name__ == "__main__":
    tt = truth_table_by_func(f)
    print("Многочлен Жегалкина:")
    print(xor_polynom(tt))
