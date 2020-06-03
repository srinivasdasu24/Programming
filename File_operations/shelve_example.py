"""

This examples explains the use of shelve module
which lets user to store data in binary format
os.path.relpath() - gives relative path
os.path.abspath() - gives absolute path
os.path.dirname() - gives directory name
os.path.basename() - gives file/folder name
os.path.isfile() - tells whether it is a file exists
os.path.exists() - checks whether file exists or not
os.path.isdir() - tells wether file is directory
os.path.mkdirs() - creates directories
os.path.isabs() - checks path is absolute path or not

"""
# useful for stroing complex data like lists,dictionary etc
import shelve

shelfile = shelve.open('mydata')
shelfile['cats']=["Zophie","pookah","simon","Fat-tail"]
shelfile.close()


shelfile = shelve.open('mydata')
shelfile['cats']

#o/p is Zophie, pookah, simon,Fat-tail

shelfile.close() 
