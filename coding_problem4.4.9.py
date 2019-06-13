#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


#Write your function here!
def get_grade(filename):
    def reader(filename):
        data = open(filename, 'r')
        tups = []
        for line in data:
            val = line.split()
            tup = (int(val[0]), val[1], int(val[2]), int(val[3]), float(val[4]))
            tups.append(tup)
        data.close()
        return tups

    values = reader(filename)
    result = 0
    for score in values:
        result += ((score[2] / score[3]) * score[4])
    return result * 100
