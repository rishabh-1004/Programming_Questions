from library import maxSubsetSum


no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    print(maxSubsetSum(array))
    
