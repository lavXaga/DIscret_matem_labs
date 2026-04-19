def sol_anecdotes(n):
    calls = []
    
    def rec(people):
        k = len(people)
        if k == 1:
            return
        if k == 2:
            calls.append((people[0], people[1]))
            return
        if k == 3:
            calls.append((people[0], people[1]))
            calls.append((people[1], people[2]))
            return
        
        # k >= 4
        first = people[0]
        rest = people[1:]
        
        rec(rest)  # рекурсивно решаем для k-1
        
        last = rest[-1]
        calls.append((first, last))
        
        if len(rest) >= 2:
            second_last = rest[-2]
            calls.append((first, second_last))
    
    rec(list(range(1, n + 1)))
    return calls
