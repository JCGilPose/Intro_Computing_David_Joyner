#Write a function called mock. mock should take one
#parameter, a string. You may assume that the string will
#have only lowercase letters and spaces.
#
#Your function should return the same string, but any letter
#at an even index should be converted to uppercase.
#
#For example: mock("abcd efgh ijkl") would return
#"AbCd eFgH IjKl".
#
#Remember, you can use the ordinal function ord() to get the
#number associated with a single letter. For example,
#ord("a") returns 97. The number associated with lowercase
#letters is always 32 larger than the number associated with
#the equivalent uppercase letter. ord("a") is 97, and
#ord("A") is 65. ord("z") is 122, and ord("Z") is 90.
#
#Remember, you can use the character function chr() to
#convert a number back to a letter. For example, chr(65) will
#return "A".
#
#HINT: Treat all characters the same initially, then worry
#about taking care of spaces afterwards.
def mock(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 != 0 or string[i] == " ":
            new_string += string[i]
        else:
            new_string += chr((ord(string[i]) - 32))
    return new_string
        
#Write your function here


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#

print(mock("abcd efgh ijkl"))
print(mock("i dont know this meme"))
