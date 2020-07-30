def array_inversion(array,size):
	count=0
	for i in range(0,size):
		for j in range(i,size):
			if(array[i]>array[j]):
				count+=1
	return count



no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    print(array_inversion(array,size))
    