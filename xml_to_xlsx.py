import pandas as pd

# Read the XML file
df = pd.read_xml('compiler.xml')   #Reading

# Write the DataFrame to an XLSX file
df.to_excel('compiler.xlsx', index=False)   #Creating

