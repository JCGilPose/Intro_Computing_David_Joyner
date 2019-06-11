#Recall Coding Problem 4.3.9 (Advanced), the free body
#diagram problem. If you were unable to solve that, we've
#included the sample answer in the dropdown in the top left
#-- feel free to use that to write your answer to this
#problem.
#
#Revise your code from that problem to use a file instead of
#a list as its parameter. Name this new function
#find_net_force_from_file. The function should take one
#parameter, the name of a file. The function should return
#the net magnitude and direction, just as it did in the other
#problem.
#
#Each line of the file will have two numbers, both integers:
#the first number will be the magnitude, and the second
#number will be the angle (in degrees, from -180 to 180).
#There will be a space between them.
#

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#Add your function here!

def find_net_force_from_file(filename):
    data = open(filename, 'r')
    magnitudes_angles = []
    for line in data:
        nums = line.split()
        magnit, angle = (int(nums[0]), int(nums[1]))
        magnitudes_angles.append((magnit, angle))
    data.close()
    total_horiz = 0
    total_vertic = 0
    for mag, ang in magnitudes_angles:
        horiz = mag * cos(radians(ang))
        total_horiz += horiz
        vertic = mag * sin(radians(ang))
        total_vertic += vertic
    total_mag = sqrt((total_vertic**2) + (total_horiz**2))
    total_angle = degrees(atan2(total_vertic, total_horiz))
    final_mag = round(total_mag, 1)
    final_angle = round(total_angle, 1)
    return (final_mag, final_angle)
