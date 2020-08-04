from library import merge_sort

no_of_test_cases=int(input())
result=[]
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    sorted_array=merge_sort(array)
    #print(sorted_array)
    print(" ".join(str(x) for x in sorted_array))
