def get_user_details():
    print("Please enter your details for the Slam Book.")
    name = input("Name: ")
    age = input("Age: ")
    favorite_color = input("Favorite Color: ")
    hobby = input("Hobby: ")
    
    # Return a dictionary of user details
    return {
        'Name': name,
        'Age': age,
        'Favorite Color': favorite_color,
        'Hobby': hobby
        }