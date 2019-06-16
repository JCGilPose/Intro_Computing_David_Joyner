#In this problem, we're giving you a file containing some real data from
#the Marta (Atlanta's subway system) database. Each line of the file is
#a record of a single ride at a specific Marta station. Riders enter and
#exit the subway system by tapping a Breeze Card against a gate at a
#specific station.
#
#You can see a preview of what the file will look like in
#marta_sample.csv in the dropdown in the top left. Note, however, that
#the real dataset is massive: over 200,000 individual rides are recorded.
#So, you're going to be dealing with some pretty big data!
#
#Each line of the file contains six items, separated by commas:
#
# - the transit day, in MM/DD/YYYY format.
# - the transit time, in HH:MM:SS format.
# - the device ID, an identifer of the gate at which the rider entered.
# - the station ID, a numeric identifier the station.
# - the use type, whether the rider was entering, exiting, etc.
# - a serial number, the unique identifier of the rider's Breeze Card.
#
#Your goal is to use this file to answer three questions:
#
# - What is the average number of Breeze Card taps per station?
# - What is the station ID of the station whose traffic is the closest
#   to that average?
# - What station has the least overall amount of traffic?
#
#Note that you will answer these questions in the fill-in-the-blank
#problems below, _not_ in this coding exercise. So, you don't have to
#programmatically find the station ID closest to the average: you could
#just print all the stations and their averages, then visually check
#which is closest to the average.
#
#To get you started, we've gone ahead and opened the file:

marta_file = open('../resource/lib/public/marta_01-18-2016.csv', 'r')
stations_file = open("stations.txt", 'r')
#You may add whatever code you want from here on to answer those three
#questions.
#
#stations_number = 0
#for line in stations_file:
#    stations_number += 1
#    
#print(stations_number, "stations in Atlanta.")
#print()

count = 0

stations_taps = {}

for line in marta_file:
    count += 1
    line = line.rstrip()
    line = line.split(",")
    if line[3] not in stations_taps:
        stations_taps[line[3]]= 1
    else:
        stations_taps[line[3]] +=1
stations_number = len(stations_taps)
average_taps = count / stations_number


print("Here are the total taps per station:")
print(stations_taps)
closest = None
ave_station = None

for station, taps in stations_taps.items():
    difference = abs(average_taps - taps)
    if closest == None:
        closest = difference
        ave_station = station
    else:
        if difference < closest:
            closest = difference
            ave_station = station
            #print(ave_station, difference)  

print()
print("The average number of taps per station is:", average_taps)
print()
            
print("The station closest to the average is station number:", ave_station)
print()

least = None
least_station = None

for station, taps in stations_taps.items():
    if least == None:
        least = taps
        least_station = station
    else:
        if taps < least:
            least = taps
            least_station = station

print("The station with the least traffic is station number:", least_station)

marta_file.close()
stations_file.close()
