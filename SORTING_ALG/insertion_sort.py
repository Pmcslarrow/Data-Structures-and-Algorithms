#insertion_sort.py

def insertion_sort(lst):
    
    for number in range(1, len(lst)):                               #For each number in range 1 through length list

        position = number                                           #saved variables of index and the value at the index
        current_value = lst[position]

        while position > 0 and lst[position - 1] > current_value:   #while index is > 0 and the item at an index before is greater than after
            lst[position] = lst[position - 1]                       #switch the two items to make them in order
            position -= 1                                           

        lst[position] = current_value                                 #Once the loop is over set the last value to the biggest
    
    return lst

if __name__ == '__main__':
    print(insertion_sort([55, 24, 3, 5, 89, 1929, 34, 4]))


"""
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
"""