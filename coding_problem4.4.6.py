#This is a long one -- our answer is 20 lines of code, but
#yours will probably be longer. That's because it's one of the
#more authentic problems we've done so far. This is a real
#problem you'll start to face if you want to start creating
#useful programs.
#
#One of the reasons that filetypes work is that everyone 
#agrees how they are structured. A ".png" file, for example, 
#always contains "PNG" in the first four characters to 
#assure the program that the file is actually a png. If these
#standards were not set, it would be hard to write programs 
#that know how to open and read the file. 
#
#Let’s define a new filetype called ".cs1301". 
#In this file, every line should be structured like so:
#
#number assignment_name grade total weight
#
#In this file, each component will meet the following
#description:
#
# - number: an integer-like value of the assignment number 
#
# - assignment_name: a string value of the assignment name
#
# - grade: an integer-like value of a student’s grade
#
# - total: an integer-like value of the total possible
#   number of points
#
# - weight: a float-like value ranging from 0 to 1 
#   representing the percent of the student’s grade this 
#   assignment is worth. All the weights should add up to 1.
#
#Each component should be separated with exactly one space. 
#A good sample file is available to view as 
#"sample.cs1301".
#
#Write a function called format_checker that accepts a 
#filename and returns True if the file contents accurately 
#conform to the described format. Otherwise the function 
#should return False. In other words, it should return True
#if:
#
# - Each line has five elements separated by spaces, AND
# - The first, third, and fourth elements are integers, AND
# - The fifth element is a decimal number, AND
# - All the fifth elements add to 1.
#
#You can make changes to test.cs1301 to test your function,
#or test it with sample.cs1301. Right now, running it on
#sample.cs1301 should return True, and on test.cs1301
#should return False.
#
#Write your function here!
def format_checker(filename):
    records = open(filename, 'r')
    total = 0
    for line in records.readlines():
        data = line.split()
        if len(data) != 5:
            records.close()
            return False
        try:
            a = int(data[0])
            b = int(data[2])
            c = int(data[3])
        except:
            records.close()
            return False
        try:
            d = float(data[4])
            total += d
        except:
            records.close()
            return False
    if total != 1:
        records.close()
        return False
    records.close()
    return True
        
