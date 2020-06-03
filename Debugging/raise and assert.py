"""
Explains raise and assert statements with examples 
- You can raise your own exceptions
- Assrtions to indetify the developers mistakes which are meant to be recovered from
- user mistakes should caught by using exceptions
"""

def boxPrint(symbol,width,height):
    if len(symbol)!=1:
        raise Exception('"Symbol" needs to be a length of 1.')
    if width <2 or height < 2:
        raise Exception('"Width" and "height" must be greater than 2')
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)
    

boxPrint('*",15,5)
boxPrint('0',5,16)


# traceback usage example

import traceback

try:
    raise Exception("This is the error message")
except:
    error=open("error_log.txt","a")
    error.write(traceback.format_exc())
    error.close()
    print("traceback info has been written to error_log.txt file")
    


# usage of assert statements

traffic_intersection = {"ns":"green","ew":"red"}
def switchLights(junction):
    for key in junction.keys():
        if junction[key] == "green":
            junction[key] = "yellow"
        elif junction[key] == "yellow":
            junction[key] = "red"
        elif junction[key] =="red":
            junction[key] = "green"
     assert 'red' in junction.values(), 'Neither light is red!' + str(junction)
     
switchlights(traffic_intersection)

    
