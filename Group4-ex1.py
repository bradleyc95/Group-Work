# group 4 exercise 1
# selection sort algorithm, time complexity O(n**2)
# Bradley Cox, Dominic Baker, Mousa Toure 


def selection_sort(array):

    print("Unsorted:", array)
    count = 1
    size = len(array)

    for i in range(size):
        min = i

        # iterate through unsorted portion of array
        for j in range(i + 1, size):
            # select minimum element
            if array[j] < array[min]:
                min = j

        # swap minimum value to current i
        (array[i], array[min]) = (array[min], array[i])
        print("Swap #", count, array)
        count += 1
    
    return array


array = [64, 27, 12, 7, 92, 83, 19, 31, 73]
print("Sorted:", selection_sort(array))


