
import xml.etree.ElementTree as ET      #Creating Aias for ease
        #Using element tree module

mytree = ET.parse("compiler.xml")       #Parsing the xml file
                    #Split into pieces

for info in mytree.findall("book"):         #Finds book tag and then

    print("\n\t\t*-*-*-Displaying Information-*-*-*\n\n"
        "Book ID:", info.attrib)        #Printing book id attribute
    auth = info.find("author").text     #Extracting the text from variable
    titl = info.find("title").text      #given in find func
    genr = info.find("genre").text      #and storing in variables
    pric = info.find("price").text
    pubd = info.find("publish_date").text
    desc = info.find("description").text

    print("Author Name:", auth,     #Now printing those extracted values
          "\nTitle:", titl,         #for each book id
          "\nGenre:", genr,
          "\nPrice:", pric,
          "\nPublish Date:", pubd,
          "\nDescription:", desc)


