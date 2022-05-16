array = [23, 4, 67, 12, 38, 1, 0]
def selection_sort(array):
    for i in range(len (array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array
print(selection_sort(array))