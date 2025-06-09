def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Find the smallest element
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap

arr = [5, 2, 9, 1, 5, 6]
selection_sort(arr)
print("Sorted array:", arr)
