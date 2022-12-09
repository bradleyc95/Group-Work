# group 4 exercise 5
# time complexity O(n)
# Bradley Cox, Dominic Baker, Mousa Toure

def containsX(string):
    # set char we are searching for, x
    char1 = "x"
    char2 = "X"
    
    # if string contains substring/char, return true
    # else return false
    if char1 in string:
        return True
    elif char2 in string:
        return True
    else:
        return False
    

    

str = "Exactly"

print(containsX(str))
print("Time complexity of O(n)")