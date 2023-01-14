# Parsing-xml-file-using-Python
Extracting specific data from an xml file by using parsing and printing it.


## Task Performed:

The task to perform was to extract different data from the xml file. The file contained different Book IDs and other details like author, price, date etc. of each of the books.
Each book tag contained further child tags. So we can either print the child tag and attributes with the help of for loop or store each of the text of provided tags and then print them. (second method done in the code)

## Modules that can be used:

Python allows parsing these XML documents using two modules namely, the xml.etree.ElementTree module and
Minidom (Minimal DOM Implementation). Parsing means to read information from a file and split it into pieces by identifying parts of that particular XML file.

## Module Used:

I have used ElementTree module in this code. Imported the module and setup a variable mytree which parses the given xml file.

## Working:

Now different methodscan be used to extract data from the file. I have used a for loop in which the text of provided tags is stored and then is printed. 

The loop runs for the number of `book` tag in the xml file, it will run for all the book tags (book ids) that are in the xml file. And all the data of each book id is stored and then displayed at the end. Each loop gives the detail of one book.
