def get_user_details():
    print("Welcome to the Slam Book! Please enter your details below.")
    
    # Collect user inputs
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    favorite_color = input("Favorite Color: ").strip()
    hobby = input("Hobby: ").strip()
    
    # Return a dictionary of user details
    return {
        'Name': name,
        'Age': age,
        'Favorite Color': favorite_color,
        'Hobby': hobby
    }

# Example usage
user_details = get_user_details()
print("\nThank you! Here are the details you provided:")
for key, value in user_details.items():
    print(f"{key}: {value}")
    