#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Write a function that tests whether a string is a palindrome.
#--------------------------------------------------------------------------------------------------
def is_palindrome(string):
    rev = str(''.join(reversed(string)))
    if string == rev:
        print(string + "'s a palindrome!")
    else:
        print(string + "'s not a palindrome!")
        
def main():
    my_string = str(input("Please enter the string to check: "))
    is_palindrome(my_string)
    
if __name__ == '__main__':
    main()