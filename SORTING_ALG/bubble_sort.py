#bubble_sort.py

def bubble_sort(lst):

    for i in range(len(lst)):
        for q in range(0, len(lst) - i - 1):
            if lst[q] > lst[q + 1]:
                lst[q], lst[q + 1] = lst[q + 1], lst[q]

    return lst


if __name__ == '__main__':
    print(bubble_sort([22, 19, 4, 65, 1, 84, 72]))