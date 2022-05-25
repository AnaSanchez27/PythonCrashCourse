# Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.
def double_word(word):
    length= (len(word))*2
    return word+word+str(length)
print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

# STRING INDEXING
# Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

def first_and_last(message):
    if not message or message[0] == message[-1]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


fruit = "Pineapple"
# access the string from nothing to 4 (index 0-4)
print(fruit[:4])
# access the string from index 4 onward(index 4- )
print(fruit[:4])

# Creating New strings
message = "A kong string with a silly typo"
# If you try to fix the typo by accesing the position where the mistake is, you'll get a type error ('str' object does not support item assignment)
message[2] ="l" 
new_message = message[0:2] + "l" + message[3:]
print(new_message)

# Using methods to access the index of a certain character
# For now, what you need to know is that this is a function that applies to a variable. And we can call it by following the variable with a dot. Let's try this a few more times.

#  the index method returns the index of the given substring, inside the string
pets = "Cats & Dogs"
pets.index("&")
# 5
pets.index("C")
# 0

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

"Mountains".upper