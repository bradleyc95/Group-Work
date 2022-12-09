# group 4 exercise 4
# time complexity O(n**2)
# Bradley Cox, Dominic Baker, Mousa Toure


def intersection(first, second):
    result = []

    # iterate through both lists via nested loop
    for i in range(len(first)):
        for j in range(len(second)):

            # compare elements at indexes i and j, one by one
            # if values are the same, insert into result list and break
            if first[i] == second[j]:
                result.append(first[i])
                # return list and end function if intersection is found
                return result
        
    # return empty list if no intersection is found
    return result


first = [1, 3, 5, 7, 9, 11, 13, 15]
second = [2, 4, 6, 7, 8, 10, 13, 14]

print(intersection(first, second))
print("Time complexity of O(n**2)")
