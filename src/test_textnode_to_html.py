import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

class TestTextNode_TO_HTML(unittest.TestCase):
    def test_text_node_to_html(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Hello, world!")
    
    def test_text_node_to_html_bold(self):
        text_node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Hello, world!</b>")
    
    def test_text_node_to_html_italic(self):
        text_node = TextNode("Hello, world!", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Hello, world!</i>")
    
    def test_text_node_to_html_code(self):
        text_node = TextNode("Hello, world!", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Hello, world!</code>")
    
    def test_text_node_to_html_link(self):
        text_node = TextNode("Hello, world!", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com">Hello, world!</a>')
    
    def test_text_node_to_html_image(self):
        text_node = TextNode("alt text", TextType.IMAGE, "https://www.example.com", "alt text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com" alt="alt text">')

if __name__ == "__main__":
    unittest.main()