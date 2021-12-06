#merge_sort.py
import random

def create_rand_lst():
    lst_len = random.randint(10, 20)
    return [random.randint(0, 100) for i in range(lst_len)]

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left, right = lst[:mid], lst[mid:]
        merge_sort(left)
        merge_sort(right)
        #Split into n leaves

        i = 0           #pointer for left
        j = 0           #pointer for right
        k = 0           #pointer for main/end list

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1

            k += 1
            
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    
    return lst




if __name__ == '__main__':
    lst = create_rand_lst()
    print('Unsorted List: ', lst)
    print('Sorted List: ', merge_sort(lst))