import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            "h1", "This is a test", "p", {"href": "www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), ' href= "www.google.com" target= "_blank"'
        )

    def test_none(self):
        node = HTMLNode()
        print(node, "none class works!")

    def test_repr(self):
        node = HTMLNode(
            "h1", "This is a test", "p", {"href": "www.google.com", "target": "_blank"}
        )
        print(node.__repr__(), "| repr works")

    def test_LeafNode(self):
        leaf_Node = LeafNode("this is my content","a",{"href": "www.google.com"})
        print(leaf_Node, "this is a leaf node ")
        self.assertEqual(leaf_Node.to_html(),f"<{leaf_Node.tag}{leaf_Node.props_to_html()}>{leaf_Node.value}</{leaf_Node.tag}>")

    #testing to html in parent node
    def test_to_html(self):
        node = ParentNode([
        LeafNode("Bold text","b" ,{"test": "how this look"}),
        LeafNode("replaced none with this"),
        LeafNode("italic text","i" ),
        LeafNode("replaced none with this", "b"),
    ],"p",{"href": "www.google.com"})
        print(node.to_html(),"***********parent node")


if __name__ == "__main__":
    unittest.main()
