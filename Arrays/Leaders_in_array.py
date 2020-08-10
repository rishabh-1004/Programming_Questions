def leaders_in_array(array):
	maximum=-1
	leaders=[]
	for i in array[::-1]:
		if(i>=maximum):
			leaders.insert(0,i)
			maximum=leaders[0]
			continue
	return leaders


no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    result=leaders_in_array(array)
    print(" ".join(str(x) for x in result))





'''
result=leaders_in_array([16,17,4,3,5,2])

print(result[::-1])
'''