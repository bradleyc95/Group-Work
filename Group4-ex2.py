# group 4 exercise 2
# time complexity O(n)
# Bradley Cox, Dominic Baker, Mousa Toure

def greatestNumber(list):

    # set max as first item in the list
    max = list[0]

    # iterate through the list, update max when a larger value is found
    for i in list:
        if max < i:
            max = i
    
    return max

list = [12, 16, 28, 10, 14, 8, 32, 11]
print(greatestNumber(list))