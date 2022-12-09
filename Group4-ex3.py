# group 4 exercise 3
# time complexity O(n)
# Bradley Cox, Dominic Baker, Mousa Toure

def hasDuplicateValue(array):
    steps = 0
    existingNumbers = [0] * (max(array) + 1)
    
    #Goes through the array to check if there is any duplicate numbers
    for x in range(len(array)):
        #Add to the number steps taken
        steps = steps + 1
        #if the number exist in the array return true
        if existingNumbers[array[x]] == 1:
          return True
          #if not then add 1 to the index
        else:
            existingNumbers[array[x]] = 1
    #print the number of steps
    print(steps)
    #if there is no duplicates return false
    return False
#hard code array
arr = [1,5,3,4,8]
#print if the array contains duplicates
print(hasDuplicateValue(arr))
print("Time complexity of O(n)")
        