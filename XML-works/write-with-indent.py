
import xml.dom.minidom

with xml.dom.minidom.parse("data/books-no-format.xml") as dom:
    pretty = dom.toprettyxml()
    # print(pretty)  # this is just a string
    pretty_dom = xml.dom.minidom.parseString(pretty)

    with open("data/books-with-format.xml", "w") as out_xml:
        pretty_dom.writexml(out_xml)
        # dom.writexml(out_xml, indent="\t", addindent="\t", newl="\n")  # this works also
