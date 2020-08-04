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

def missing_element_in_array(arr, n):
    return int((n*(n+1))/2 - sum(arr))

def SubArraySum(size,final,array):
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
        print(-1)


def rearrange_alternate_array(arr):
    c=[]
    for i in range(0,len(arr)):
        if(i%2==0):
            c.append(max(arr))
            arr.remove(max(arr))
        else:
            c.append(min(arr))
            arr.remove(min(arr))
    return(c)


def merge_sort(A):
    n=len(A)
    if n == 1 :
        return A
    mid = n // 2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L,R)

def merge(L,R):
    i=0
    j=0
    answer=[]
    while (i<len(L) and j<len(R)):
        if L[i]<R[j]:
            answer.append(L[i])
            i+=1
        else:
            answer.append(R[j])
            j+=1
    if  (i<len(L)):
        answer.extend(L[i:])
    if (j<len(R)):
        answer.extend(R[j:])
    return answer