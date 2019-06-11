#Write a function called average_file. average_file should
#have one parameter: a filename.
#
#The file should have an integer on each line. average_file
#should return the average of these integers. However, if
#any of the lines of the file are _not_ integers,
#average_file should return the string "Error reading file!"
#
#Remember, by default, every time you read a line from a
#file, it's interpreted as a string.


#Add your function here!
def average_file(filename):
    total = 0
    count = 0
    data = open(filename, 'r')
    for line in data:
        try:
            total += int(line)
            count += 1
        except:
            data.close()
            return "Error reading file!"
    data.close()
    return (total / count)
