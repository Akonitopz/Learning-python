def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if the element is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps were made, stop the loop
            break

arr = [5, 2, 9, 1, 5, 6, 3, 4]
bubble_sort(arr)
print("Sorted array:", arr)
