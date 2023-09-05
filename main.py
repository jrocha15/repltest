# String Practice:

# Create a Python program that asks the user to input a sentence.
# Print the first and last letter of the sentence.
# Convert the entire sentence to uppercase and print the result.
# Find and print a substring from the inputted sentence.
# Replace a word in the sentence and print the updated sentence.
sentence = input("Tell me about yourself:")
print(f'{sentence}')
print(sentence[0])
print(sentence[16])
print(sentence.upper())
print(sentence[8:13])
print(sentence.replace("15", "16"))

# Input Practice:

# Create a Python program that asks the user for their name, age, and favorite movie.
# Print a message back to the user with this information.
# Note: Make sure to convert the age to an integer.
name = input("What is your name?")
age = input("What is your age?")
favorite_movie = input("What is your favorite movie?")
print(
    f'Hello {name}! You are {age} years old. Your favorite movie is {favorite_movie}.'
)

# F-String Practice:

# Create a Python program that asks the user for three objects in the room.
# Create variables from these objects and insert those variables into an f-string sentence.
# Print the f-string sentence.
objects = input("Name 3 objects in the room.")
object_1 = "computers"
object_2 = "a clock"
object_3 = "keyboards"
print(f'In room 318, you will find {object_1}, {object_2}, and {object_3}.')
# Advanced String Practice:

# Create a Python program that reverses the words in a sentence inputted by the user.
# For example, if the user inputs "Python is fun", the program should print "fun is Python".
# Advanced Input Practice:
word = input("What do you think of python?")
print(f'{word}')

# Create a Python program that asks the user for the name of their favorite book, movie, and song.

# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."

# Advanced F-String Practice:

# Create a Python program that asks the user for their name, age, and the current year.
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."

# Type Conversion Practice:

# Create a Python program that asks the user for two numbers.
# Print the sum, difference, product, and quotient of the two numbers.
# Note: Make sure to convert the input to integers before performing any calculations.

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
# Print the length of the summary.
# Uppercase the entire summary and print it.
# Replace a word in the summary and print the updated summary.
# Print the last word of the summary.

# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."
