arr=[87,179,181,981,107,175,187]
min= arr.index(min(arr))
max= arr.index(max(arr))
arr[min], arr[max] = arr[max], arr[min]
print('Массив после перестановки минимального и максимального элементов ', arr)