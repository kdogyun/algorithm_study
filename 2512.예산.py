import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().rstrip().split()))
budgets.sort()
m = int(input())

sBudget = sum(budgets)
if m >= sBudget:
    print(budgets[-1])
else:
    max_budget = 0
    ac_m = m
    rest = float('inf')
    for idx, b in enumerate(budgets):
        ac_m -= b
        length = len(budgets) - 1 - idx
        if length == 0:
            continue
        temp = int(ac_m / length)
        if length != 0 and ac_m >= 0 and temp > max_budget:
            a = 0
            for i in range(idx+1, len(budgets)):
                if budgets[i] >= temp:
                    a += temp * (len(budgets) - 1 - i)
                    break
                else:
                    a += budgets[i]
            if rest >  ac_m - a:
                rest =  ac_m - a
                max_budget = temp
    print(max_budget)