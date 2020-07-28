from library import missing_element_in_array

no_of_test_cases=int(input())
for i in range(0,no_of_test_cases):
    size=int(input())
    array = [int(i) for i in input().split()]
    print(missing_element_in_array(array,size))