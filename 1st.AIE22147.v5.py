def find_pairs_with_sum(arr, target):
    length = len(arr)
    pairs = []

    # Iterate through each element in the array
    for i in range(length):
        # Iterates through elements after the current element
        for j in range(i + 1, length):
            # Checks if the sum of the pair is equal to the target
            if arr[i] + arr[j] == target:
                # Increment count for each pair found
                pairs.append((arr[i], arr[j]))

    return pairs

def main():
    my_list = []
    num_elements = int(input("Enter the number of elements in the list: "))

    # Get user input for each element in the list
    for i in range(num_elements):
        element = int(input(f"Enter element {i + 1}: "))
        my_list.append(element)

    target_sum = int(input("Enter the target sum: "))
    
    # Find and display pairs with the target sum
    pairs = find_pairs_with_sum(my_list, target_sum)
    
    if not pairs:
        print("No pairs found with the given target sum.")
    else:
        print(f"Pairs with the target sum {target_sum}: {pairs}")

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()
