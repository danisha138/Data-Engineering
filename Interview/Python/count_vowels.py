# Define the input string
input_string = "Hello, WOrld!"

# Define the vowels
vowels = "aeiouAEIOU"

# Initialize a dictionary to store vowel counts
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Loop through each character in the input string
for char in input_string:
    # Check if the character is a vowel
    if char in vowels:
        # Increment the count for the respective vowel
        vowel_counts[char.lower()] += 1

# Display the result
for vowel, count in vowel_counts.items():
    print(f"The count of {vowel} is: {count}")


PS C:\Users\Admin> & "C:/Program Files/Python312/python.exe" c:/Users/count_vowels.py
The count of a is: 0
The count of e is: 1
The count of i is: 0
The count of o is: 2
The count of u is: 0
