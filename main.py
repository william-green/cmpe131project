import sys
import csv
import json
import xml.etree.ElementTree as ET

# Read the command line arguments
filename = sys.argv[1]
format = sys.argv[2]

# Read the tab delimited data from the file
with open(filename, 'r') as file:
    data = [line.strip().split('\t') for line in file]

# Convert the data to the specified format
if format == '-c':
    # Convert to CSV
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
elif format == '-j':
    # Convert to JSON
    json_data = [dict(zip(data[0], row)) for row in data[1:]]
    with open('output.json', 'w') as file:
        json.dump(json_data, file, indent=4)
elif format == '-x':
    # Convert to XML
    root = ET.Element('data')
    for row in data[1:]:
        element = ET.SubElement(root, 'row')
        for i, col_name in enumerate(data[0]):
            sub_element = ET.SubElement(element, col_name)
            sub_element.text = row[i]
    tree = ET.ElementTree(root)
    tree.write('output.xml')

print('File converted to', format, 'format and saved in the current directory.')
