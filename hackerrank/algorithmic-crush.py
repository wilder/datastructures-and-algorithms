def get_max(n, m):
    l = [0] * n
    for _ in range(m):
        a, b, k = map(int, raw_input().split())
        for i in range(a-1, b):
            l[i] += k
    return max(l)


n, m = map(int, raw_input().split())
print get_max(n, m)
