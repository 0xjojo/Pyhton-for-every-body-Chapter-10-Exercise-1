'''Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.'''
import string
letter_dict = dict()
letter_list = list()
dec_list = list()
file_name = input ("Enter a file name:")
if len(file_name) < 1:
    file_name = 'romeo.txt'
try :
    file_handle = open (file_name)
except:
    print (file_name , "The file could not be opened!!!" )
    quit()
line = file_handle.read()
line = line.rstrip()
line = line.translate(line.maketrans('','',string.punctuation))
line = line.translate(line.maketrans('','',string.digits))
line = line.translate(line.maketrans('','',' '))
line = line.lower()
print (line)
for l in line:
    letter_list.append(l)
    if l not in letter_dict:
        letter_dict[l] =1
    else :
        letter_dict[l] += 1
for key  in letter_dict:
    dec_list.append((letter_dict[key],key))
dec_list.sort(reverse=True)
print (dec_list)
