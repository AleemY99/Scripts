def nextpal(value):
    value = [int(i) for i in str(value+1)]
    
    l = len(value)
    for i in range(l//2):
        value[-i-2] += value[i] < value[-i-1]
            
        for j in reversed(range(l-i-1)):
            value[j-1] += value[j] // 10
            value[j] %= 10
            
        value[-i-1] = value[i]
    
    return "".join([str(i) for i in value])

if __name__ == "__main__":
    print(nextpal(3))
    print(nextpal(721382))
    print(nextpal(10241193))
    print(nextpal(3849551))
    print(nextpal(3**39))