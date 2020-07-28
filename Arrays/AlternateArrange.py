from library import rearrange_alternate_array

no_of_test_cases=int(input())
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    result=rearrange_alternate_array(array)
    print(" ".join(str(x) for x in result))

'''
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    li = stdin.readline().split()
    mx = 0
    for l in li:
        if int(l) > mx:
            mx = int(l)
    mx += 1
    minindex = 0
    maxindex = n - 1
    for i in range(n):
        if i % 2:
            li[i] = int(li[i]) + (int(li[minindex]) % mx) * mx
            minindex += 1
        else:
            li[i] = int(li[i]) + (int(li[maxindex]) % mx) * mx
            maxindex -= 1
    for j in li:
        print(j // mx,end = " ")
    stdout.write("\n")
'''