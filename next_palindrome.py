fliphalf1 = lambda x: x[:len(x)//2] + x[-1:(len(x)//2)-1:-1] 
fliphalf2 = lambda x: x[:(len(x)//2)+1] + x[-1:len(x)//2:-1]

def nextpal(n):
    x = [] # Makes an array to separate the digits of n
    for i in str(n):
        x.append(i)

    if(len(x) % 2 == 0): # The string operations required for an even number
        for idx, val in enumerate(x[0:len(x)//2]):
            x[len(x)//2 + idx] = val # Turns the second half of the number into a copy of the first (e.g. 127355 becomes 127127)
        x = fliphalf1(x) # Flips the second half of the number

        a_string = "".join(x)
        an_integer = int(a_string) # Gives us x as one integer to compare to our original n
        for i in range(0, len(x)):
            x[i] = int(x[i]) # Turns x into a list of integers rather than strings to perform arithmetic on

        if(an_integer <= n): # Corrects x if it is less than our original n (we want the next palindrome not the previous)
            x[len(x)//2] += 1
            x[len(x)//2 - 1] += 1
        
        string = [str(integer) for integer in x] # Turns x back into a list of integers, concatenates, and converts back to an integer
        a_string2 = "".join(string)              
        ansEven = int(a_string2) # Our answer

        return ansEven
    else: # The string operations required for an odd number
        for idx, val in enumerate(x[0:len(x)//2]):
            x[len(x)//2 + 1 + idx] = val 
        x = fliphalf2(x)

        string2 = [str(integer) for integer in x] 
        a_string3 = "".join(string2)
        an_integer2 = int(a_string3)

        for i in range(0, len(x)):
            x[i] = int(x[i])

        if(an_integer2 <= n):
            x[len(x)//2 - 1] += 1
            x[len(x)//2 + 1] += 1
            x[len(x)//2] = 0
        
        string3 = [str(integer) for integer in x]
        a_string4 = "".join(string3)
        ansOdd = int(a_string4)
        
        return ansOdd

if __name__ == "__main__":
    print(nextpal(1221))
    print(nextpal(10241193))
    print(nextpal(3849551))
    print(nextpal(3**39))