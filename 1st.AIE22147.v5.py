def find_pairs_with_sum(arr, target):
    length = len(arr)
    pairs = []
#goes through each element in the array
    for i in range(length):
        # goes through elements after the current element
        for j in range(i + 1, length):
            #if the sum of the pair is equal to the target then it adds in the pairs array.
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

def main():
    my_list = []
    num_elements = int(input("Enter the number of elements in the list:: "))

    # using for loops to get user input for each element in the list
    for i in range(num_elements):
        element = int(input(f"Enter the element {i + 1}: "))
        my_list.append(element)
O
    target_sum = int(input("Enter the sum: "))
    
    # Find and display pairs with the target sum
    pairs = find_pairs_with_sum(my_list, target_sum)
    
    if not pairs:
        print("sorry, no such pairs have been forund in the given list...")
    else:
        print(f"pairs of the sum {target_sum}: {pairs}")
main()
