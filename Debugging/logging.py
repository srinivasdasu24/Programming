"""
How to use logging in python with examples
different log levels 
logging.debug() - at debug level
logging.info() - for info
logging.warning() - warning
logging.error() - for error
logging.critical()  - critical level

"""

import logging

logging.basicConfig(filename="my_log.txt",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

# by giving file name we can write to file , otherwise written to screen



# factorial program with logging

import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # log levels - disable all level logging

logging.debug("start of the program")
def factorial(n):
  logging.debug("starting of the factorial %s",%(n))
  total=1
  for i in range(1,n+1):
    total*=i
    loggind.debug('i is %s, total is %s',%(i,total))
  logging.debug("Return value is %s,%(total))
  return total
  
print(factorial(5))
logging.debug("end of the program")
