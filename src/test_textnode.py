import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_noteq(self):
        node = TextNode("This is a textnode", TextType.ITALIC)
        node2 = TextNode("This is another textnode", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_true_noteq_text(self):
        node = TextNode("random text", TextType.CODE)
        node2 = TextNode("other text", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_truenoteq_texttype(self):
        node = TextNode("Random text", TextType.BOLD)
        node2 = TextNode("Random text", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    


if __name__ == "__main__":
    unittest.main()