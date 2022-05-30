# Havel Hakimi Theorem

def remove0(arr):
    return list(filter(lambda num: num != 0, arr))

def descending(arr):
    arr.sort()
    return arr[::-1]

def frontElim(n, arr):
    for idx, i in enumerate(arr):
        if idx < n:
            arr[idx] = i - 1
    return arr

def HH(ans):
    while(True):
        ans = remove0(ans)
        if len(ans) == 0:
            return True
  
        ans = descending(ans)
        N = ans[0]
        ans.remove(N)
        if len(ans) < N:
            return False
      
        ans = frontElim(N, ans)

if __name__ == "__main__":
    print(HH([5,3,0,2,6,2,0,7,2,5]))
    print(HH([2,2,2,2,2]))