"""
Takes in array from the user
divides the length of the array into two until only value exits in each array
compares its self to nearby arrays
merges total output

"""



def merge_sort(arr):

    red_flag = False
    i = 1

    if len(arr) <= 1:
        return arr
    
    while i < len(arr):
        if(arr[i] < arr[i - 1]):
            red_flag = True
        i += 1
        
    if (not red_flag) :
        return arr
    else :

        mid = len(arr) // 2

        left_side = arr[:mid]
        right_side = arr[mid:]

        # print(len(arr))

        l = merge_sort(left_side)
        r = merge_sort(right_side)
        # print(l)
        # print(r)

        return merge(l, r)

"""Function that does the merging of the arrays"""

def merge(a, b):

    sorted_array = []

    x = 0 
    y = 0 

    len_a = len(a) 
    len_b = len(b) 

    while x < len_a and y < len_b:

        if a[x] <= b[y]:
            sorted_array.append(a[x])
            x += 1
            
        else:
            sorted_array.append(b[y])
            y += 1  
                  
        
    while x < len_a:
        sorted_array.append(a[x])
        x += 1
        

    while y < len_b:
        sorted_array.append(b[y])
        y += 1
        

        # print(sorted_array)

    return sorted_array





