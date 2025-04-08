def oddCollatz(n):
    result = []
    
    while n >= 1:
        if n % 2 == 1:
            result.append(n)
            
        if n == 1:
            break
            
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            
    return result

print(oddCollatz(1))
print(oddCollatz(3))
print(oddCollatz(5))
print(oddCollatz(7))