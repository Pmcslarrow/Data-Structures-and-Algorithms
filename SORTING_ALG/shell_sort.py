#shell_sort.py

def shell_sort(lst):
    gap = len(lst) // 2
    while gap > 0:

        for num in range(gap):
            gap_insertion(lst, num, gap)
        
        gap //= 2
    
    return lst



def gap_insertion(alist, start, gap):
    
    for i in range(start+gap, len(alist), gap):

        position = i
        current_value = alist[i]

        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = current_value
        
    return alist
    



if __name__ == '__main__':
    print(shell_sort([89, 24, 3, 5, 55, 1929, 34, 4]))