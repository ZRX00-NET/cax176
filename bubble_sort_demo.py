#define list
bubble_sort = [64, 25, 12, 22, 11]
# set to true so loop can run
swap = True

while swap:
    swap = False
    for i in range(len(bubble_sort)-1):
        if bubble_sort[i] > bubble_sort[i+1]:
            #if the first digit is bigger than the second
            bubble_sort[i], bubble_sort[i+1] = bubble_sort[i+1], bubble_sort[i]
            #change position
            swap = True

print(bubble_sort)