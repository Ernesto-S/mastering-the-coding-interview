# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique(any_string):
    unique = None
    index = 1
    print(f"\nDoes {any_string} have all unique characters? (yes/no)\n")
    for character in any_string:
        if character in any_string[index:len(any_string)]:
            unique = "no"
            return unique
        index += 1
    unique = "yes"
    return unique
        
print(is_unique("Rudolph"))

print(is_unique("Reindeer"))