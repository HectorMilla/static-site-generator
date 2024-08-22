import unittest

from textnode import TextNode
from htmlnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_url(self):
        node = TextNode("This is a text node","bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node,node2)
    def test_text_type(self):
        node = TextNode("This is a text node","italic","https://boot.dev")
        node2 = TextNode("This is a text node", "italic","https://boot.dev")
        self.assertEqual(node,node2)
    def test_not_eq(self):
        node = TextNode("This is a text node","italic","https://boot.dev")
        node2 = TextNode("This is a text node", "bold","https://boot.dev")
        self.assertNotEqual(node,node2)
    #TRYING TO FIX OUTPUT OF TEST
    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node","italic","https://boot.dev")
        node2 = TextNode("This is a text node","italic")
        self.assertEqual(text_node_to_html_node(node2).to_html(),"<i>This is a text node</i>")
if __name__ == "__main__":
    unittest.main()