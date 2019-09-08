'''Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1'''
d = dict()
lst = list()
file_name = input("Enter a file name:")
if (len(file_name)<1):
    file_name = 'mbox-short.txt'
try:
    file_handle = open(file_name)
except:
    print ("the file could not be opened")
    quit()
for line in file_handle:
    line = line.rstrip()
    words = line.split()
    for word in words :
        if (words[0]!='From' ):
             continue
        else :
            time = words[5]
            time = time.split(':')

            if time[0] not in d :
                d[time[0]] = 1
            else:
                d[time[0]] += 1

for hour  in d :
    lst.append((hour , d[hour]))
lst.sort()
for hour , count in lst:
    print (hour , count)
