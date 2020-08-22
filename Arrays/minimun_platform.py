from library import minimum_platform


no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
	details=[int(i) for i in input().split()]
	size=int(details[0])
	array = [int(i) for i in input().split()]
	array2= [int(i) for i in input().split()]
	result=minimum_platform(array,array2)
	print(result)



#array1=[900,940,950,1100,1500,1800]
#array2=[910,1200,1120,1130,1900,2000]

#array1=[900,1100,1235]
#array2=[1000,1200,1240]