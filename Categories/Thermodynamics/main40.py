def binary_search_property(table, property_name, value):
    low, high = 0, len(table) - 1
    while low <= high:
        mid = (low + high) // 2
        if table[mid][property_name] < value:
            low = mid + 1
        elif table[mid][property_name] > value:
            high = mid - 1
        else:
            return table[mid]  # Found the exact value
    return None  # Value not found

# Sample thermodynamic table
table = [
    {"T": 300, "P": 100, "v": 0.001},  # Example data
    {"T": 350, "P": 200, "v": 0.002},
    {"T": 400, "P": 300, "v": 0.003},
    {"T": 450, "P": 400, "v": 0.004}
]

result = binary_search_property(table, "T", 350)
if result:
    print(f"Found property at T = 350K: {result}")
else:
    print("Property not found")
