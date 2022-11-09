'''
select a pivot, ie a number among the sequence of numbers to sort
create two list
append numbers less than pivot to one list and those greater to other list
perform action iteratively until sorting is done
'''


def quicksort(unsorted_list):
    length = len(unsorted_list)
    if length <= 1:
        return unsorted_list
    else:
        pivot = unsorted_list.pop()    #to use as pivot for comparision
    print(pivot)
    numbers_greater_than_pivot = []
    numbers_less_than_pivot =  []

    for i in unsorted_list:
        if i < pivot:
            numbers_less_than_pivot.append(i)
        else:
            numbers_greater_than_pivot.append(i)
    
    
    return quicksort(numbers_less_than_pivot) + [pivot] + quicksort(numbers_greater_than_pivot)

test1 = [2,1,7,8,5,6,3,9,4,1]
print(quicksort(test1))


