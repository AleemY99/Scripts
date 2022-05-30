def fib_sum(): 
    ans = 0
    x = 0 # Represents the current Fibbonaci number being processed
    y = 1 # Represents the next Fibbonaci number being processed
    while x <= 4000000:
        if x % 2 == 0:
            ans += x
        x, y = y, (x + y)
    return ans