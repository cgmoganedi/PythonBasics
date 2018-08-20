import xml.etree.ElementTree as ET
my_tree = ET.parse('my_data.xml')
root = my_tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag)

for i in range(10):
    print(root[i])

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')

a.write('newfile2.xml')
