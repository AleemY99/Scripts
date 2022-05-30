def gcd(a, b): # Function to return gcd of two integers
    while b != 0:
        (a, b) = (b, a % b)
    return a

def phi(n): # Euler totient function
    ans = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            ans += 1
    return ans