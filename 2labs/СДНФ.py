def f(x, y, z):
    return x or (not y) or z


def truth_table():
    res = []
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                res.append((x, y, z, int(f(x, y, z))))
    return res


def sdnf():
    terms = []
    for x, y, z, val in truth_table():
        if val == 1:
            term = []
            term.append("x" if x else "¬x")
            term.append("y" if y else "¬y")
            term.append("z" if z else "¬z")
            terms.append("(" + " ∧ ".join(term) + ")")
    return " ∨ ".join(terms)


if __name__ == "__main__":
    print("СДНФ для f(x,y,z) = x ∨ ¬y ∨ z:")
    print(sdnf())
