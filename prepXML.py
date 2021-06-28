import lxml.etree as et

FILE_PATH = './FILEPATH'
XML_ATTRIBUTE = 'ATTRIBUTE_NAME'

sync_db_name_value = 'get_attribute_value_for_sync'

tree = et.parse(FILE_PATH)

for attribute in tree.xpath(XML_ATTRIBUTE):

    if attribute.get(sync_db_name_value)[0] == '_':
        new_db_name = attribute.get(sync_db_name_value)[1:]
    else:

        new_db_name = attribute.get(sync_db_name_value)

    print("New DB name: ", new_db_name)
    attribute.set('db_name', new_db_name)

tree.write('output.xml')

