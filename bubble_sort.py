def bubblesort(unsorted_list):
    length = len(unsorted_list)
    for i in range(length-1):        # last item not needed to be compared
        print(i)
        for j in range(length-1-i):  # after an iteration, the highest number is sent to the last position, so no need to compare them. this is more efficient
            print(j)
            
            if unsorted_list[j] > unsorted_list[j+1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = temp
                '''
                for the code above, we can also swap using the snipet below
                unsorted_list[j], unsorted_list[j+1] =unsorted_list[j+1], unsorted_list[j]
                '''
        print(unsorted_list)
        print(' ')

    return unsorted_list

