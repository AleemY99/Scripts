# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

set1 = []
for i in range(100, 1000):
    set1.append(i)
set2 = set1

products = []
for num1 in set1:
    for num2 in set2:
        products.append(num1 * num2)

palindromes = []
for p in products:
    if len(str(p)) == 5:
        if str(p)[0] == str(p)[4] and str(p)[1] == str(p)[3]:
            palindromes.append(int(p))
    if len(str(p)) == 6:
        if str(p)[0] == str(p)[5] and str(p)[1] == str(p)[4] and str(p)[2] == str(p)[3]:
            palindromes.append(int(p))

ans = max(palindromes)
print(ans)