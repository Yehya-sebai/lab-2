import xml.dom.minidom as minidom
with open('currency.xml', 'r', encoding='windows-1251') as xml_file:
    xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()
valute_elements = dom.getElementsByTagName('Valute')
char_codes = []
values = []
for valute_element in valute_elements:
    char_code = valute_element.getElementsByTagName('CharCode')[0].firstChild.data
    value = valute_element.getElementsByTagName('Value')[0].firstChild.data
    char_codes.append(char_code)
    values.append(float(value.replace(',', '.')))  
print("CharCodes:", char_codes)
print("Values:", values)
