# Python has built-in string validation methods for basic data. 
# It can check if a string is composed of alphabetical characters, 
# alphanumeric characters, digits, etc.

# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s)) 
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))