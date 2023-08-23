def reverse(string):
    new_string = ""
    for i in range(len(string)):
        new_string += string[len(string) - i - 1]
    return new_string
    
def reverse_2(string):
    return reverse(string)
    
def reverse_3(string):
    return string[8::-1]
    
string = "hong dang"
