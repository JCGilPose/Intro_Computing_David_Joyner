#Write a function called st_dev. st_dev should have one
#parameter, a filename. The file will contain one integer on
#each line. The function should return the population standard
#deviation of those numbers.
#
#The formula for population standard deviation can be found here:
#edge.edx.org/asset-v1:GTx+gt-mooc-staging1+2018_T1+type@asset+block@stdev.PNG
#
#The formula is a bit complex, though, and since this is a
#CS class and not a math class, here are the steps you would
#take to calculate it manually:
#
# 1. Find the mean of the list.
# 2. For each data point, find the difference between that
#    point and the mean. Square that difference, and add it
#    to a running sum of differences.
# 4. Divide the sum of differences by the length of the
#    list.
# 5. Take the square root of the result.
#
#You may assume for this problem that the file will contain
#only integers -- you don't need to worry about invalid
#files or lines. The easiest way to take the square root is
#to raise it to the 0.5 power (e.g. 2 ** 0.5 will give the
#square root of 2).
#
#Add your function here!

def st_dev(filename):
    data = open(filename, 'r')
    total = 0
    count = 0
    mean = 0
    nums = []
    diff_sum = 0
    for line in data:
        total += int(line)
        count += 1
        nums.append(int(line))
    mean = total / count
    for num in nums:
        diff_sum += ((num - mean)**2)
    diff_sum /= count
    data.close()
    return diff_sum**0.5
