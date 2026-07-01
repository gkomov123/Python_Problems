# Problem
# Write a function that determines if two strings are anagrams 
# (contain the exact same characters in a different order).

def isanagram(first_word:str, second_word:str) -> bool:
    return True if sorted(first_word) == sorted(second_word) else False




word1 = "listen"
word2 = "silent"

print(isanagram(word1, word2))