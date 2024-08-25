import unittest

from textnode import TextNode
from htmlnode import text_node_to_html_node
from split_nodes_delimeter import split_nodes_delimiter, extract_markdown_images
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
    
    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node","italic","https://boot.dev")
        node2 = TextNode("This is a text node","italic")
        self.assertEqual(text_node_to_html_node(node2).to_html(),"<i>This is a text node</i>")
    
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` bb", "text")
        node1 = TextNode("This is a bold word **OMGEA** yeahhh","text")
        split_nodes_delimiter([node,node1],"**","bold")
        self.assertEqual(split_nodes_delimiter([node],"`", "code"),[
      TextNode("This is text with a ", "text"),
     TextNode("code block", "code"),
     TextNode(" bb", "text"),
])
        
    def test_extract_markdown_images(self):
        self.assertEqual(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"),[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")] )
if __name__ == "__main__":
    unittest.main()