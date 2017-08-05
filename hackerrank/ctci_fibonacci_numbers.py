def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
        
n = int(raw_input())
print(fibonacci(n))
