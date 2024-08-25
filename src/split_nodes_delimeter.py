# function to split markdown into nodes
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    #keep writing this function try to edit code to see how splitting the text in the node will look like2
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_node[i], text_type_text))
            else:
                split_nodes.append(TextNode(split_node[i],text_type))
        new_nodes.extend(split_nodes)
        print(new_nodes)
    return new_nodes