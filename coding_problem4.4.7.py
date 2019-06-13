#Write a function called "reader" that reads in a ".cs1301" 
#file described in the previous problem. The function should 
#return a list of tuples representing the lines in the file like so:
#
#[(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight), 
#(line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
#
#All items should be of type int except for the name (string) 
#and the weight (float). You can assume the file will be in the 
#proper format -- in a real program, you would use your code
#from the previous problem to check for formatting before
#trying to call the function below.
#
#Write your function here!
def reader(filename):
    data = open(filename, 'r')
    tups = []
    for line in data:
        val = line.split()
        tup = (int(val[0]), val[1], int(val[2]), int(val[3]), float(val[4]))
        tups.append(tup)
    data.close()
    return tups
