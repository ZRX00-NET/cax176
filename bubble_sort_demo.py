bubble_sort = [64, 25, 12, 22, 11]
swap = True

while swap:
    swap = False
    for i in range(len(bubble_sort)-1):
        if bubble_sort[i] > bubble_sort[i+1]:
            bubble_sort[i], bubble_sort[i+1] = bubble_sort[i+1], bubble_sort[i]
            swap = True

print(bubble_sort)
