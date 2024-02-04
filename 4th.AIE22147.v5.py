def count_characters(input_string):
    # Counting the occurence of each character on the given string    
    char_count = {}
    for i in input_string:
        if i in char_count:
            char_count[i] += 1#it stores the no of occurence of the charecter in the array.
        else:
            char_count[i] = 1 #if it doesnt repeat it keeps the occurence as 1 only.
    return char_count

def find_highest_occurrence(char_count):
    # form the ount_charecters function we determine the highest occured charecter.
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    return max_char, max_count # returns the max count and max char 

def count_highest_occurrence(input_string):
    # calls the clean string function
    cleaned_string = clean_string(input_string)
    char_count = count_characters(cleaned_string)    
    # returns the character with highest occurrence
    max_char, max_count = find_highest_occurrence(char_count)
    return max_char, max_count

def clean_string(input_string):
    # this function removes non-alphabetic characters, converts the string to lowercase
    return ''.join(char.lower() for char in input_string if char.isalpha())

##########################################################
input_string = input("Enter the string: ")
max_char, max_count = count_highest_occurrence(input_string)
def count_characters(input_string):
    # Counting the occurence of each character on the given string    
    char_count = {}
    for i in input_string:
        if i in char_count:
            char_count[i] += 1#it stores the no of occurence of the charecter in the array.
        else:
            char_count[i] = 1 #if it doesnt repeat it keeps the occurence as 1 only.
    return char_count

def find_highest_occurrence(char_count):
    # form the ount_charecters function we determine the highest occured charecter.
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    return max_char, max_count # returns the max count and max char 

def count_highest_occurrence(input_string):
    # calls the clean string function
    cleaned_string = clean_string(input_string)
    char_count = count_characters(cleaned_string)    
    # returns the character with highest occurrence
    max_char, max_count = find_highest_occurrence(char_count)
    return max_char, max_count

def clean_string(input_string):
    # this function removes non-alphabetic characters, converts the string to lowercase
    return ''.join(char.lower() for char in input_string if char.isalpha())

##########################################################
input_string = input("Enter the string: ")
max_char, max_count = count_highest_occurrence(input_string)
print(f"The maximum occurring character: '{max_char}' \n Occurrence count: {max_count}.")
