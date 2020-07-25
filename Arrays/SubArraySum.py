
def checkSum(size,final,array):
		first=0
		total=0
		i=0
		for i in range(0,size+1):
			while (total>final and first<i-1):
				total=total-array[first]
				first+=1
			if total==final:
				print (first+1,i)
				return(1)
			if i<size:
				total=total+array[i]

		print (-1)
		


no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
	details=[int(i) for i in input().split()]
	size, final=int(details[0]) , int(details[1])
	array = [int(i) for i in input().split()]
	#print(final,array)
	checkSum(size,final,array)
	
#42 468
#135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134
