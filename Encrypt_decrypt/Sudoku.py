'''
Estimated time

60 minutes
Level of difficulty

Hard
Objectives

    improving the student's skills in operating with strings and lists;
    converting strings into lists.

Scenario

As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

    each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
    each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
    each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

If you need more details, you can find them here.

Your task is to write a program which:

    reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
    outputs Yes if the Sudoku is valid, and No otherwise.

Test your code using the data we've provided.
Test data

Sample input:

295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

Sample output:
Yes

Sample input:

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

Sample output:
No
'''

class sudoku():
    b = []
    sud = 'Yes'
    def board(s):
        x = ''
        s = 'x' + s
        for _ in range(1,len(s)):
            x += s[_]
            if (_ % 9) == 0:
                sudoku.b.append(x)
                x = ''
        return(sudoku.b)

    def hor(b):
        for _ in b:
            for q in _:
                if _.count(q) > 1:
                    sudoku.sud = 'No'
                    break

    def ver(b):
        n = []
        j = ''
        for _ in range(len(b[0])):
            for x in range(len(b)):
                j += b[x][_]
            n.append(j)
            j =''
        sudoku.hor(n)

    def box(b):
        n = []
        j = ''
        for _ in range(0, len(b), 3):
            for x in range(0, len(b[0]), 3):
                for q in range(3):
                    for i in range(3):
                        j += (b[_+q][x+i])
                n.append(j)
                j = ''
        sudoku.hor(n)


## Example

s = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"
#s = "195743862431865927876192543387459216612387495549216738763524189928671354254938671"

sd = sudoku.board(s)
sudoku.hor(sd)
sudoku.ver(sd)
sudoku.box(sd)
print(sudoku.sud)