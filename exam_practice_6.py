#Write a function called are_anagrams. The function should
#have two parameters, a pair of strings. The function should
#return True if the strings are anagrams of one another,
#False if they are not.
#
#Two strings are considered anagrams if they have only the
#same letters, as well as the same count of each letter. For
#this problem, you should ignore spaces and capitalization.
#
#So, for us: "Elvis" and "Lives" would be considered
#anagrams. So would "Eleven plus two" and "Twelve plus one".
#
#Note that if one string can be made only out of the letters
#of another, but with duplicates, we do NOT consider them
#anagrams. For example, "Elvis" and "Live Viles" would not
#be anagrams.


#Write your function here!

def are_anagrams(string_1, string_2):
    lower_1 = string_1.lower()
    lower_2 = string_2.lower()
    words_1 = lower_1.split(' ')
    words_2 = lower_2.split(' ')

    chars_1 = []
    chars_2 = []
    for word in words_1:
        for i in range(len(word)):
            chars_1.append(word[i])
    for word in words_2:
        for i in range(len(word)):
            chars_2.append(word[i])
    
    for i in chars_1:
        if i in chars_2:
            chars_2.remove(i)
    if len(chars_2) == 0:
        return True

    return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False, each on their own line.
print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))
