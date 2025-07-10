# Reverse a string using loop and with recursion

def recursive_reverse_string(str):
    if str == "":
        return str
        
    return recursive_reverse_string(str[1:]) + str[0]
    

def loop_reverse_string(str):
    reversed = ""
    for i in range(len(str)-1,-1,-1):
        reversed += str[i]
    return reversed
    


print("Recursive")
print(recursive_reverse_string("yoyo"))


print("Loops")
print(loop_reverse_string("yoyo master"))