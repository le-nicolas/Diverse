def quicksort(arr, property_name):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[property_name] < pivot[property_name]]
    middle = [x for x in arr if x[property_name] == pivot[property_name]]
    right = [x for x in arr if x[property_name] > pivot[property_name]]
    return quicksort(left, property_name) + middle + quicksort(right, property_name)

# Unsorted thermodynamic table
unsorted_table = [
    {"T": 450, "P": 400, "v": 0.004},
    {"T": 300, "P": 100, "v": 0.001},
    {"T": 350, "P": 200, "v": 0.002},
    {"T": 400, "P": 300, "v": 0.003}
]

sorted_table = quicksort(unsorted_table, "T")
print("Sorted table by temperature:", sorted_table)
