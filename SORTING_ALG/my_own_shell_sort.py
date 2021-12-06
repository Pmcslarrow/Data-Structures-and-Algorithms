def shell(lst):

    gap = len(lst) // 2

    while gap > 0:
        
        for start in range(gap):

            for i in range(start + gap, len(lst), gap):

                current_value = lst[i]
                position = i

                while position >= gap and lst[position - gap] > current_value:
                    lst[position] = lst[position - gap]
                    position = position - gap
                
                lst[position] = current_value

        gap //= 2

    return lst

if __name__=='__main__':
    print(shell([89, 24, 3, 5, 55, 1929, 34, 4]))