'''Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line.
 Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195'''
import string
d = dict()
lst = list()
file_name =input ("Enter a file name:")
if (len(file_name) < 1):
    file_name = 'mbox-short.txt'
file_handle = open (file_name)
for line in file_handle:
    line = line.rstrip()
    #line = line.translate(line.maketrans('','',string.punctuation))
    words = line.split()
    if len(words) < 1: continue
    if words[0] != 'From': continue
    else :
        email = words[1]
        if email not in d :
            d[email] = 1
        else :
            d[email] = d[email] + 1
for email in d:
    lst.append((d[email],email))
lst.sort(reverse=True)
for (count , email) in lst[:1]:
    print (email , count) 
