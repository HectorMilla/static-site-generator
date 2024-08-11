import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            "h1", "This is a test", "p", {"href": "www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), ' href: "www.google.com"  target: "_blank" '
        )

    def test_none(self):
        node = HTMLNode()
        print(node, "none class works!")

    def test_repr(self):
        node = HTMLNode(
            "h1", "This is a test", "p", {"href": "www.google.com", "target": "_blank"}
        )
        print(node.__repr__(), "| repr works")


if __name__ == "__main__":
    unittest.main()
