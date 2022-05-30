def gpf(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = int(n / i)
        i += 1
    return n

print(gpf(600851475143))