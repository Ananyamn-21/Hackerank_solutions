# You are given a string and your task is to swap cases. 
# In other words, convert all 
# lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
                
    return result
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)