import math

def maxSubsetSum(A):
    max_start, max_stop = 0, 1 # Start, Stop of maximum sub-array
    curr = 0                   # pointer to current array
    max_sum = A[0]         # Sum of maximum array
    current_sum = 0            # sum of current array

    for i, elem in enumerate(A):
        current_sum +=  elem

        if max_sum < current_sum:
            max_sum = current_sum 
            max_start = curr
            max_stop = i  + 1
        if current_sum < 0:
            current_sum = 0
            curr = i + 1

    return  max_sum
    '''
    dp = []
    for i in range(0, len(a)):
        if i == 0:
            dp.append(a[i])
            print(dp)
        elif i == 1:
            dp.append(max(dp[0], dp[0]+a[i],a[i]))
            print(dp)
        else:
            dp.append(max(dp[i - 1], dp[i - 2], dp[i - 2] + a[i]))
            print(dp[i - 1], dp[i - 2], dp[i - 2] + a[i])
            print(dp)
    return dp[len(a) - 1]
    '''
print(maxSubsetSum([1,2,3]))

'''
no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    print(maxSubsetSum(array))
    
'''