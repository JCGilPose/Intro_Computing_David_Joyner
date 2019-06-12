#Do not change the line of code below. It's at the top of
#the file to ensure that it runs before any of your code.
#You will be able to access french_dict from inside your
#function.
french_dict = {"me": "moi", "hello": "bonjour", 
               "goodbye": "au revoir", "cat": "chat", 
               "dog": "chien", "and": "et"}

#Write a function called french2eng that takes in one string
#parameter called sentence. french2eng should look at each
#word in the sentence and translate it into French if it is
#found in the dictionary, french_dict. If a word is not found
#in the dictionary, do not translate it: use the original
#word. Then, the function should return a string of the
#translated sentence.
#
#You may assume that the sentence you're translating has no
#punctuation. However, you should convert it to lower case
#before translating.
#
#For example:
#
#  french2eng("Hello it's me") -> "bonjour it's moi"
#

#Write your function here!
def french2eng(sentence):
    translated = sentence.lower()
    words = translated.split()
    output = ""
    for word in words:
        if word in french_dict:
            output += (french_dict[word] + " ")
        else:
            output += (word + " ")
    return output

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: bonjour it's moi
print(french2eng("Hello it's me"))
