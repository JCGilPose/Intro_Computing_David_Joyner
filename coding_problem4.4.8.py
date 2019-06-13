#Write a function called write_1301 which will write a file
#in the format described in Coding Problem 4.4.2. The
#sample.cs1301 file has been included to refresh your 
#memory. Your function should accept two arguments:
#A string of a filename to write to, and a list of tuples. 
#You can assume that each tuple will have the following 
#format:
#
#(int, str, int, int, float)
#
#Each tuple will represent a line in the file, and each
#item in the tuple should correspond to the 
#assignment number, the assignment name, the student's 
#grade, the total possible number of points, and the 
#assignment weight respectively. 


#Write your function here!
def write_1301(filename, data):
    records = open(filename, 'w')
    for tup in data:
        string = ""
        for val in tup:
            val = str(val)
            string += val + " "
        print(string.rstrip(), file=records)
    records.close()
