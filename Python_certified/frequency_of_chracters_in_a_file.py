'''
Objectives

    improving the student's skills in operating with files (reading)
    using data collections for counting numerous data.

Scenario

A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

    asks the user for the input file's name;
    reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
    prints a simple histogram in alphabetical order (only non-zero counts should be presented)

Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:
aBc

the expected output should look as follows:
a -> 1
b -> 1
c -> 1

Tip:

We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.

'''
from os import strerror
dict_i ={}
srcname = input("Source file name: ")
try:
    src = open(srcname, 'rt')
    ch = src.read(1)
    while ch != '':
        if ch.isalpha():
            if ch.lower() not in dict_i:
                dict_i[ch.lower()] = 1
            else:
                dict_i[ch.lower()] += 1
        ch = src.read(1)
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)

for i in sorted(dict_i):
    if dict_i[i] > 0:
        print((i, dict_i[i]), sep="->")



# Sort the charcter frequency by its count

from os import strerror
dict_i ={}
srcname = input("Source file name: ")
try:
    src = open(srcname, 'rt')
    ch = src.read(1)
    while ch != '':
        if ch.isalpha():
            if ch.lower() not in dict_i:
                dict_i[ch.lower()] = 1
            else:
                dict_i[ch.lower()] += 1
        ch = src.read(1)
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)

dict_i=sorted(dict_i.items(),key = lambda kv:(kv[1], kv[0]),reverse=True)
for x,y in (dict_i):
    if y > 0:
        print((x, y), sep="->")