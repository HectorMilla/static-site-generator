import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            "h1", "This is a test", "p", {"href": "www.google.com", "target": "_blank"}
        )
        node.props_to_html()


if __name__ == "__main__":
    unittest.main()
