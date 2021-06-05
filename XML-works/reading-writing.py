
import xml.etree.ElementTree as ET

tree = ET.parse('data/books2.xml')
root = tree.getroot()

# add a new book tag to xml - version two
# book = ET.Element("book", attrib={'id': 'bk114'}) # works also
book = ET.Element("book")
book.set('id', 'bk114')

author = ET.SubElement(book, "author")
author.text = "Test Author 2"

title = ET.SubElement(book, "title")
title.text = "Test title 2"

genre = ET.SubElement(book, "genre")
genre.text = "Test genre 2"

price = ET.SubElement(book, "price")
price.text = "48.25"

publish_date = ET.SubElement(book, "publish_date")
publish_date.text = "2001-04-26"

description = ET.SubElement(book, "description")
description.text = "Test description 2"

root.append(book)

tree.write('data/books2.xml')

# add a new book tag to xml - version one
# book = ET.fromstring(
#     """<book id="bk113">
#         <author>Test Author</author>
#         <title>Test title</title>
#         <genre>Test genre</genre>
#         <price>50.95</price>
#         <publish_date>2001-08-15</publish_date>
#         <description>Test description</description>
#     </book>"""
# )
# root.append(book)


# deletes the hash attributes on book tags
# for book in tree.findall('book'):
#     del(book.attrib['hash'])
#
# tree.write('data/books2.xml')

# creates a hash attribute on book tags
# _id = 1
# for book in tree.findall('book'):
#     book.set('hash', 'some-hash' + str(_id))
#     _id += 1
#
# tree.write('data/books2.xml')


# # adds the created attribute to the root, see books2.xml
# root.set('created', '1-1-2021')
# tree.write('books2.xml')


# for genre in root.findall('book/genre'):
#     print(genre.text)

# for book in root.iter('book'):
#     print(book.attrib)
#     print(book[0].text)

# for book in root.findall('book'):
#     price = book.find('price').text
#     print(price)

