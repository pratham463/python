def is_disarium(number):
    # Convert the number to a string to access individual digits
    digits = str(number)
    length = len(digits)
    
    # Calculate the sum of digits powered by their positions
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(digits))
    
    # Check if the sum equals the original number
    return disarium_sum == number

# Input from the user
num = int(input("Enter a number: "))

# Check and display the result
if is_disarium(num):
    print(f"{num} is a Disarium number!")
else:
    print(f"{num} is not a Disarium number.")