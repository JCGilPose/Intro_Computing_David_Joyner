#Write a function called count_types. count_types
#should take as input a single string, and return a
#dictionary. In the dictionary, the keys should be
#types of characters, and the values should be the
#number of times each type of character appeared in
#the string.
#
#The types of characters that should be handled (and
#thus, the keys in the dictionary) are:
#
# - upper: the count of upper-case or capital letters
# - lower: the count of lower-case letters
# - punctuation: the count of punctuation characters.
#   You may assume this is limited to these punctuation
#   characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# - space: the count of spaces
# - numeral: the count of numerals, 0123456789
#
#Note, however, that any type of character that does
#NOT appear in the string should not be in the dictionary
#at all.
#
#For example:
#
#count_characters("aabbccc") -> 
# {"lower": 7}
#count_characters("ABC 123 doe ray me!") -> 
# {"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
#
#Because the first string has only lower-case letters,
#"lower" is the only key in the dictionary.
#
#Write your function here!
def count_types(string):
    chars = {}
    uppers = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lowers = "qwertyuiopasdfghjklzxcvbnm"
    puncts = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"'''
    a_space = " "
    nums = "0123456789"
    for i in string:
        if i in uppers:
            if "upper" not in chars.keys():
                chars["upper"] = 1
            else:
                chars["upper"] += 1
        elif i in lowers:
            if "lower" not in chars.keys():
                chars["lower"] = 1
            else:
                chars["lower"] += 1
        elif i in puncts:
            if "punctuation" not in chars.keys():
                chars["punctuation"] = 1
            else:
                chars["punctuation"] += 1
        elif i == a_space:
            if "space" not in chars.keys():
                chars["space"] = 1
            else:
                chars["space"] += 1
        elif i in nums:
            if "numeral" not in chars.keys():
                chars["numeral"] = 1
            else:
                chars["numeral"] += 1
    return chars


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"lower": 7}
#{"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))
