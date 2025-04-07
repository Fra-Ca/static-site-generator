import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_2_to_html(self):
        node = LeafNode("b", "This is some text")
        self.assertEqual(node.to_html(), "<b>This is some text</b>") 

if __name__ == "__main__":
    unittest.main()