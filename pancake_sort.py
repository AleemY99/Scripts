"""
Given an array of integers, sort the array (smallest to largest) using the flipfront function on the entire array. For example, the array:
[3, 1, 2, 1]
may be sorted with three calls to flipfront:
flipfront([3, 1, 2, 1], 4) => [1, 2, 1, 3]
flipfront([1, 2, 1, 3], 2) => [2, 1, 1, 3]
flipfront([2, 1, 1, 3], 3) => [1, 1, 2, 3]

Make sure you correctly handle elements that appear more than once in the array!

You may not modify the array by any other means, but you may examine it however you want. 
You can even make a copy of the array and manipulate the copy, including sorting it using some other algorithm.
Try to minimize the number of times you call flipfront while sorting. Note that this is different from minimizing the runtime of your program.
"""

flipfront = lambda x, k: x[k-1::-1] + x[k:]

def pancake_sort(x):
    i = 0
    while i < len(x):
        x = flipfront(x, x.index(max(x[0:(len(x)-i)])) + 1)
        x = flipfront(x, len(x) - i)
        i += 1
    return x

if __name__ == "__main__":
    x = [3, 2, 1, 4, 2, 5, 0]
    print(pancake_sort(x))