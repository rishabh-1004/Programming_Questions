def solution(arr, n):
	return int((n*(n+1))/2 - sum(arr))

no_of_test_cases=int(input())
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    print(solution(array,size))