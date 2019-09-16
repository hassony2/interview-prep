def rec_fibonacci(n):
    if n <= 1:
        return n
    else:
        return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)

def mem_fibonacci(n, hash_fib):
    if n <= 1:
        return n
    if n - 1 in hash_fib:
        prev = hash_fib[n - 1]
    else:
        prev = mem_fibonacci(n - 1, hash_fib)
        hash_fib[n - 1] = prev

    if n - 2 in hash_fib:
        pre_prev = hash_fib[n - 2]
    else:
        pre_prev = mem_fibonacci(n - 2, hash_fib)
        hash_fib[n - 2] = pre_prev
    return prev + pre_prev

def tab_fibonacci(n):
    tab = [None] * n
    if n <= 1:
        return n
    for i in range(n):
        if i <= 1:
            tab[i] = i
        else:
            tab[i] = tab[i - 1] + tab[i - 2]
    return tab[n - 1] + tab[n - 2]


if __name__ == "__main__":
    fib_num = 4
    rec_fib_4 = rec_fibonacci(fib_num)
    mem_fib_4 = mem_fibonacci(fib_num, {})
    tab_fib_4 = tab_fibonacci(fib_num)
    print(rec_fib_4, mem_fib_4, tab_fib_4)
    for fib_num in range(20):
        # print(f"{fib_num}: {rec_fibonacci(fib_num)}, {mem_fibonacci(fib_num, {})}, {tab_fibonacci(fib_num)}")
        print("{}: {} {} {}".format(fib_num, rec_fibonacci(fib_num), mem_fibonacci(fib_num, {}), tab_fibonacci(fib_num)))

