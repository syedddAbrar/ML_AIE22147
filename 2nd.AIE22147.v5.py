def range_of_list(user_list, m):
    # Check if the list has less than or equal to 3 elements
    if m <= 3:
        return "It's not possible to determine the range."
    else:
        # Get user input for the list
        user_list_input(user_list, m)
        
        # Calculate the minimum and maximum values in the list
        minimum = min(user_list)
        maximum = max(user_list)
        
        # Calculate and return the range between the largest and smallest number
        return maximum - minimum

def user_list_input(user_list, m):
    # Get user input for each element in the list
    for i in range(0, m):
        element = int(input(f"Enter the {i + 1} element: "))
        user_list.append(element)
    return user_list

# Get the number of elements in the list from the user
num_elements = int(input("Enter the number of elements in the list: "))
user_list = []

# Display the range between the largest and smallest number in the list
print(f"The range between the largest and smallest number is {range_of_list(user_list, num_elements)}")
