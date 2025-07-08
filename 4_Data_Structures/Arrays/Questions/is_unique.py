# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique(any_string):
    unique = None
    index = 1
    for character in any_string:
        if character in any_string[index:len(any_string)]:
            unique = False
            return unique
        index++
    unique = True
    return unique
        
print(f"Does 'Rudolph' have unique characters? \n{is_unique('Rudolph')})