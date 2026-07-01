# PROBLEM 
# Create a function that takes a string and returns a count of how many times each character appears. 
# Ignore spaces and make it case-insensitive.
from collections import Counter

def char_freq_counter(some_chars:str) -> dict:
    clean_text = some_chars.lower().replace("", "")
    
    return Counter(clean_text)

text = "Python Programming"

print(char_freq_counter(text))