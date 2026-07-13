bubble_sort = [64, 25, 12, 22, 11]
lenght = len(bubble_sort)

for i in range(len(bubble_sort)-1):
    if bubble_sort[i] > bubble_sort[i+1]:
        swap = True
        bubble_sort[i], bubble_sort[i+1] = bubble_sort[i+1], bubble_sort[i]
    else:
        continue
print(bubble_sort)
