def get_turn_count(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n-1) // 2 + 1

        count += 1

    return count


r = get_turn_count(17)
print(r)
