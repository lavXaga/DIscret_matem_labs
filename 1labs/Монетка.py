def sol_coins(n):
    # Рекурсивный поиск фальшивой монеты
    def find_fake(coins):
        if len(coins) == 1:
            return coins[0]
        
        # Делим монеты на 3 группы (максимально равные)
        size = len(coins)
        part1_size = size // 3
        part2_size = size // 3
        
        group1 = coins[:part1_size]
        group2 = coins[part1_size:part1_size + part2_size]
        group3 = coins[part1_size + part2_size:]
        
        # Взвешиваем первую и вторую группы
        w = weigh(set(group1), set(group2))
        
        if w == 0:
            # Фальшивая в третьей группе
            return find_fake(group3)
        elif w == 1:
            # Фальшивая в первой группе
            return find_fake(group1)
        else:  # w == 2
            # Фальшивая во второй группе
            return find_fake(group2)
    
    # Запускаем поиск на всех монетах от 1 до n
    return find_fake(list(range(1, n + 1)))
