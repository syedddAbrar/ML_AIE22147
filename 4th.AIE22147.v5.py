def clean_string(input_string):
    # Remove non-alphabetic characters and convert to lowercase
    return ''.join(char.lower() for char in input_string if char.isalpha())

def count_characters(input_string):
    # Count the occurrences of each character in the input string
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def find_highest_occurrence(char_count):
    # Find the character with the highest occurrence in the char_count dictionary
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    return max_char, max_count

def count_highest_occurrence(input_string):
    # Clean the input string and count character occurrences
    cleaned_string = clean_string(input_string)
    char_count = count_characters(cleaned_string)
    
    # Find and return the character with the highest occurrence
    max_char, max_count = find_highest_occurrence(char_count)
    return max_char, max_count

# Get user input for the string
input_string = input("Enter the string: ")

try:
    # Attempt to find and display the highest occurring character and its count
    max_char, max_count = count_highest_occurrence(input_string)
    print(f"The highest occurring character: '{max_char}' \n Occurrence count: {max_count}.")
except ValueError as e:
    # Handle any potential errors
    print(f"Error: {e}")
