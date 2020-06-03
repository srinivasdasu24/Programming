"""

Performing read and write operations on pdf files 
pip install PyPDF2

"""

import PyPDF2
import os

file_name=open("file_name","rb")
reader=PyPDF2.PdfFileReader(file_name)
reader.numPages

page = reader.getPage(0)
text=page.extractText()


for page in range(reader.numPages):
    print(reader.getPage(page)).extractText())
    
 
# merging two pdf files data

file1 = open("file_name","rb
file2 = open("file_name2","rb")
reader1=PyPDF2.PdfFileReader(file1)
reader2=PyPDF2.PdfFileReader(file2)

writer = PyPDF2.PdfFileWriter()  # it will create a empty file which is in current memory not in systems memory

for page in range(reader1.numPages):
    writer.addPage(reader1.getPage(page))
    
for page in range(reader2.numPages):
    writer.addPage(reader2.getPage(page))
    
    
 outputFile = open("file_name","wb")
 writer.write(outputFile)
 outputFile.close()
 file1.close()
 file2.close()




