import struct

# Read the binary file (ECU dump)
def read_ecu_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data

# Modify fuel map data (This is an illustrative example)
def modify_fuel_map(data, offset, new_value):
    # Assuming fuel map data is at a specific offset and value is a float
    modified_data = bytearray(data)
    struct.pack_into('<f', modified_data, offset, new_value)  # '<f' = little-endian float
    return modified_data

# Save modified ECU file
def save_modified_ecu(file_path, modified_data):
    with open(file_path, 'wb') as file:
        file.write(modified_data)

# Usage Example
original_data = read_ecu_file('original_ecu.bin')
modified_data = modify_fuel_map(original_data, offset=0x1234, new_value=0.95)  # Adjust fuel to 95%
save_modified_ecu('modified_ecu.bin', modified_data)
