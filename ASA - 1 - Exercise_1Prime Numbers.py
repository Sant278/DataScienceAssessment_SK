#!/usr/bin/env python
# coding: utf-8

# In[7]:


def is_prime(number):
    # Check if number is less than 2, which is not a prime number
    if number <= 1:
        return False    
    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:  # If divisible, it's not a prime number
            return False    
    # If no divisors are found, the number is prime
    return True
# Input from the user
num = int(input("Enter a number: "))

# Check and display whether the number is prime or not
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# In[ ]:


#Code Functioning:
	The is_prime function checks whether the number n given as input is prime.
	It first addresses numbers 1 and below, which don't qualify as prime.
It eliminates all even numbers greater than 2 and numbers that are divisible by 3.
 It then checks factors starting from 5 up to the square root of n, increasing by 6 each time to test numbers in the form 6k ±1.
You can run this on any Python platform. Just enter a number when prompted, and it will tell you whether it is prime.


# In[10]:


import random

def main():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Calculate the correct product
    correct_product = num1 * num2

    # Ask the user to input the product of the two numbers
    user_answer = int(input(f"What is the product of {num1} and {num2}? "))

    # Check if the user's answer is correct
    if user_answer == correct_product:
        print("Correct! Well done.")
    else:
        print(f"Sorry, the correct answer is {correct_product}.")

# Run the program
main()


# In[ ]:


# This program works as follows: -
I. The program uses the random module to create two random whole numbers from 1 to 10.
II. It calculates the product of these two numbers.
III. It prompts the user to input his/her answer.
IV. The program compares the user's answer with the right result and displays a message telling whether the answer is correct or not.


# In[11]:


# Choosing to work with even numbers within the range 100 to 200

# Loop through the range from 100 to 200
for num in range(100, 201):
    # Check if the number is even
    if num % 2 == 0:
        # Print the square of the even number
        print(f"The square of {num} is {num**2}")


# In[ ]:


#This is how the function works:
• print_squares_of_evens needs two inputs: start and end.
• It goes through all numbers between start and end.
• It makes a check whether it is possible to divide each number by 2 with no remainder.
• For such numbers, it multiplies the number by itself and prints the result.


# In[12]:


import string

def count_words(input_text):
    # Remove punctuation (using str.translate and string.punctuation)
    input_text = input_text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the input text into words
    words = input_text.split()

    # Create a dictionary to store word counts
    word_count = {}

    # Iterate over the words and count occurrences
    for word in words:
        word = word.lower()  # Convert word to lowercase to count case-insensitively
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Print word counts
    for word, count in word_count.items():
        print(f"'{word}': {count}")

# Example usage
input_text = "This is a sample text. This text will be used to demonstrate the word counter."
count_words(input_text)


# In[ ]:


#How it works:
• The function count_words takes a string text.
• It converts the text to lowercase and splits it into words.
•   A dictionary word_count keeps the count of every word.
•   Remove common punctuation from each word (like periods, commas, etc.).
•   Increment the count for each word within the dictionary
•   Finally, return the dictionary word counts
You can run the program with some sample text, and it will yield the word count of each word.


# In[13]:


import string

def is_palindrome(input_string):
    # Remove punctuation, spaces, and convert the string to lowercase
    input_string = input_string.lower()
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))
    input_string = input_string.replace(" ", "")
    
    # Check if the string reads the same forward and backward
    return input_string == input_string[::-1]

# Example usage
input_text = "racecar"
print(is_palindrome(input_text))  # Expected Output: True


# In[ ]:


#Process –
The is_palindrome function takes as argument a string called input_string

It preprocesses the string by performing the following operations on it:
Converts the string to lowercase.
Removes all non-alphanumeric characters, including punctuation and spaces.
It then checks if the preprocessed string reads the same forward and backward by comparing it to its reverse, which is preprocessed_string [:-1].
Returns True if the string is a palindrome and False otherwise.
You can call this function with different parameters to test for palindromes.

