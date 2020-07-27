def merge_sorted_array(a,b):
	i=0
	j=0
	c=[]
	while (i<len(a) and j<len(b)):
		if(a[i]<b[j]):
			c.append(a[i])
			i+=1
		else:
			c.append(b[j])
			j+=1
	while(i<len(a)):
		c.append(a[i])
		i+=1
	while(j<len(b)):
		c.append(b[j])
		j+=1
	return(c)




no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
	details=[int(i) for i in input().split()]
	size, size2=int(details[0]) , int(details[1])
	array = [int(i) for i in input().split()]
	array2= [int(i) for i in input().split()]
	#print(final,array)
	result=merge_sorted_array(array,array2)
	print(" ".join(str(x) for x in result))

