data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "profession": "Engineer"
}

# Prompt user to enter a key
key = input("Enter the key to find its value: ")

# Check if the key exists in the dictionary
if key in data:
    print(f"The value for the key '{key}' is: {data[key]}")
else:
    print(f"Key '{key}' not found in the dictionary.")
