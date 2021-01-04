import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

def two_pow(num):
    a = 0
    b = 0
    temp = num
    while int(temp/2) != 0:
        a+=1
        temp = int(temp/2)
    under = a + (num - 2**a)
    high = a+1 - (num - 2**(a+1))

    if under <= high:
        return a, num - 2**a
    else:
        return a+1, abs(num - 2**(a+1))

n_pow, n_count = two_pow(n)
k_pow, k_count = two_pow(k)

print(min(abs(abs(n)-abs(k)), abs(n_pow-k_pow)+n_count+k_count))