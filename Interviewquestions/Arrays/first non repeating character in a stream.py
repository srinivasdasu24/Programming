'''

    Author: Dasu Srinivas
    Description : Find first non-repeating character in a stream

'''

MAX_CHAR = 256


def firstNonRepeating(stream):
    DDL = [] * MAX_CHAR
    repeat = [False] * MAX_CHAR
    for c in range(0, len(stream)):
        if not repeat[ord(stream[c])]:
            if not stream[c] in DDL:
                DDL.append(stream[c])
            else:
                DDL.remove(stream[c])

        if len(DDL) != 0:
            print("non-repeating character so far:", DDL[0])


firstNonRepeating("srinivasrndasu")
