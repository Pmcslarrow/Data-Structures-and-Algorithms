#selection_sort.py

def selection_sort(lst):

    for number in range(len(lst) - 1, 0, -1):
        max_num_position = 0
        for position in range(1, number + 1):
            if lst[position] > lst[max_num_position]:
                max_num_position = position
        
        temp = lst[number] 
        lst[number] = lst[max_num_position]
        lst[max_num_position] = temp

    return lst

if __name__ == '__main__':
    print(selection_sort([55, 24, 3, 5, 89, 1929, 34, 4]))