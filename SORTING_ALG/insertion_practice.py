def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        current_value = lst[i]
        while j >= 0 and current_value < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current_value
    return lst

if __name__ == '__main__':
    answer = insertion_sort([5, 6, 1, 7, 9, 22, 3, 2, 44, 30])
    print(answer)