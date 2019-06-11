#Write a function called "angry_file_finder" that accepts a
#filename as a parameter. The function should open the file,
#read it, and return True if the file contains "!" on every
#line. Otherwise the function should return False. 
#
#Write your function here!
def angry_file_finder(filename):
    the_file = open(filename, 'r')
    for line in the_file:
        if "!" not in line:
            the_file.close()
            return False
    the_file.close()
    return True
