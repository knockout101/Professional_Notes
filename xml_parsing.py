import xml.etree.ElementTree


cars_for_sale = xml.etree.ElementTree.parse('cars.xml')

print(cars_for_sale.write())

for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    print(repr(car))
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
        print(' =', prop.text)

cars = cars_for_sale.find('car')
print()

