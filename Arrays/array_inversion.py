'''
def array_inversion(array,size):
	count=0
	for i in range(0,size):
		for j in range(i,size):
			if(array[i]>array[j]):
				count+=1
	return count
'''

def mergeSortInversion(arr):
	if(len(arr)==1):
		return arr,0
	else:
		print(arr)
		s=len(arr)//2
		a=arr[0:s]
		b=arr[(len(arr)//2):]

		a,ai=mergeSortInversion(a)
		b,bi=mergeSortInversion(b)
		c=[]

		i=0
		j=0
		inversions=0+ai+bi

	while i<len(a) and j<len(b):
		if(a[i]<b[j]):
			c.append(a[i])
			i+=1
		else:
			c.append(b[j])
			j+=1
			inversions+= (len(a)-i)
	c+=a[i:]
	c+=b[j:]

	return c, inversions



no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    c,inversions=mergeSortInversion(array)
    print(inversions)
    