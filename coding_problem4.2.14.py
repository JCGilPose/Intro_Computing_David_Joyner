#In the previous problem, you wrote a function that would
#convert text like "abcd efgh ijkl" into "AbCd eFgH IjKl".
#
#In the previous problem, you could assume the original
#string would be all lower-case, with no punctuation.
#
#Revise your function so that it no longer makes these
#assumptions. It should leave any punctuation marks or
#numerals unchanged, and it should change the case of
#every letter at an even index. That means if the letter
#is initially uppercase, it should be converted to lower
#case.
#
#For example: mock("Abcd. Efgh.. Ijkl!") would return
#"abCd. efGh.. IJkL!". The even-index letters (A, C, E, g,
#j, l) changed case, all other characters were unchanged.
#
#HINT: Lowercase letters always have an ordinal between
#97 ("a") and 122 ("z"). Uppercase letters always have an
#ordinal between 65 ("A") and 90 ("Z").


#Write your function here!
def mock(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 != 0:
            new_string += string[i]
        elif ord(string[i]) > 96 and ord(string[i]) < 123:
            new_string += chr(ord(string[i]) - 32)
        elif ord(string[i]) > 64 and ord(string[i]) < 91:
            new_string += chr(ord(string[i]) + 32)
        else:
            new_string += string[i]
    return new_string


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#
print(mock("Abcd. Efgh.. Ijkl!"))

