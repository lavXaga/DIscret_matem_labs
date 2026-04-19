def sol_cookies(n):
    # База для 60..65
    base = {
        60: (10, 0),
        61: (8, 1),
        62: (6, 2),
        63: (4, 3),
        64: (2, 4),
        65: (0, 5)
    }
    
    if n in base:
        return base[n]
    
    # Рекурсивный спуск: n -> n-6
    a, b = sol_cookies(n - 6)
    return (a + 1, b)
