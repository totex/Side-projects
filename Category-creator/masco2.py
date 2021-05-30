import csv
from pprint import pprint
from nodes import Node

CATEGORY_INDEX = 10  # list index of the category text
CATEGORY_SEPARATOR = ">"

all_categories = []
hierarchies = list()
hierarchies.append(Node(1, "Katalógus", "root", 0))


# Reads the CSV category text into the all_categories list
def read_categories():
    category_hashes = []
    with open("data/MascoHU.csv", "r", encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        header = next(spamreader)

        # cat_code = 2  # cat code 1 is "Katalógus"
        for row in spamreader:
            category_list = row[CATEGORY_INDEX].split(CATEGORY_SEPARATOR)
            inner_list = []

            for cat in category_list:
                cat_text = cat.strip()  # strip the spaces after text
                inner_list.append(cat_text)

            cat_hash = "".join(inner_list[1:])  # drop the first [1:] 'Kategóriák'
            if cat_hash not in category_hashes:

                category_hashes.append(cat_hash)
                all_categories.append(inner_list[1:])  # drop the first [1:] 'Kategóriák'


# Prints out the hierarchies list
def show_nodes():
    for node in hierarchies:
        print(node)


# Checks if category name already exists in the hierarchies list
def does_node_exists(cat_name):
    for node in hierarchies:
        if node.name == cat_name:
            return True
    return False


def find_parent_id(cat_name, list_index):
    '''
    list_index is the current index into the inner list of all_categories
    example: [[Kaputelefon, CODEFON], [Gyári cserealkatrészek, FAAC]]
    when list_index == 0, it will return [Kaputelefon, CODEFON]
    when list_index == 1, it will return [Gyári cserealkatrészek, FAAC] and so on
    '''

    # all_categories[list_index].index("Gyári cserealkatrészek") -> returns the index number of "Gyári cserealkatrészek"
    index_by_name = all_categories[list_index].index(cat_name)

    # This returns for the name, for example: "Gyári cserealkatrészek"
    name = all_categories[list_index][index_by_name - 1]

    for node in hierarchies:
        if node.name == name:
            return node.id


def create_hierarchy():
    cat_code = 2
    for index1, cat in enumerate(all_categories):
        for index2, cat_name in enumerate(cat):
            if not does_node_exists(cat_name):
                node_type = 'node' if len(cat)-1 != index2 else 'leaf'
                if index2 == 0:
                    parent = 1  # the parent is 1 when index2 is 0
                else:
                    parent = find_parent_id(cat_name, index1)  # TODO - looks like it works :) - have to use index1
                hierarchies.append(Node(cat_code, cat_name, node_type, parent))
                cat_code += 1


read_categories()
create_hierarchy()
show_nodes()
# pprint(hierarchies)
# pprint(all_categories)

