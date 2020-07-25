import math

def maxSubsetSum(A):
    max_start, max_stop = 0, 1 
    curr = 0                  
    max_sum = A[0]        
    current_sum = 0           

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

no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    print(maxSubsetSum(array))
    
