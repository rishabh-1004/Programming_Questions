from library import merge_sorted_array

no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
	details=[int(i) for i in input().split()]
	size, size2=int(details[0]) , int(details[1])
	array = [int(i) for i in input().split()]
	array2= [int(i) for i in input().split()]
	result=merge_sorted_array(array,array2)
	print(" ".join(str(x) for x in result))

