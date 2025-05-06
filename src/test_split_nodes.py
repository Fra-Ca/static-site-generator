import unittest
from split_nodes_images import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links
import re

class TestSplitNodesImages(unittest.TestCase):
    def test_split_nodes_image(self):
        # Create a textnode with some images inside
        node = TextNode("This is text with an ![alt text](image.png) image", TextType.TEXT)
        # Split it using the image delimiter
        result = split_nodes_image([node])
        # Check the result
        self.assertEqual(len(result), 3)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with an ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "alt text")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "image.png")
        self.assertEqual(result[2].text, " image")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    def test_split_nodes_image_with_no_image(self):
        # Create a textnode with no images inside
        node = TextNode("This is just text", TextType.TEXT)
        # Split it using the image delimiter
        result = split_nodes_image([node])
        # Check the result
        self.assertEqual(len(result), 1)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is just text")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    def test_split_nodes_image_with_empty_string(self):
        # Create a textnode with an empty string
        node = TextNode("", TextType.TEXT)
        # Split it using the image delimiter
        result = split_nodes_image([node])
        # Check the result
        self.assertEqual(len(result), 1)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    def test_split_nodes_image_with_multiple_images(self):
        # Create a textnode with multiple images inside
        node = TextNode("This is text with an ![alt text](image.png) image and ![another image](another.png)", TextType.TEXT)
        # Split it using the image delimiter
        result = split_nodes_image([node])
        # Check the result
        self.assertEqual(len(result), 5)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with an ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "alt text")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "image.png")
        self.assertEqual(result[2].text, " image and ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "another image")
        self.assertEqual(result[3].text_type, TextType.IMAGE)
        self.assertEqual(result[3].url, "another.png")
        self.assertEqual(result[4].text, "")
        self.assertEqual(result[4].text_type, TextType.TEXT)
    def test_split_nodes_link(self):
        # Create a textnode with some links inside
        node = TextNode("This is text with a [link text](http://example.com) link", TextType.TEXT)
        # Split it using the link delimiter
        result = split_nodes_link([node])
        # Check the result
        self.assertEqual(len(result), 3)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "link text")
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "http://example.com")
        self.assertEqual(result[2].text, " link")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    def test_split_nodes_link_with_no_link(self):
        # Create a textnode with no links inside
        node = TextNode("This is just text", TextType.TEXT)
        # Split it using the link delimiter
        result = split_nodes_link([node])
        # Check the result
        self.assertEqual(len(result), 1)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is just text")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    def test_split_nodes_link_with_empty_string(self):
        # Create a textnode with an empty string
        node = TextNode("", TextType.TEXT)
        # Split it using the link delimiter
        result = split_nodes_link([node])
        # Check the result
        self.assertEqual(len(result), 1)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    def test_split_nodes_link_with_multiple_links(self):
        # Create a textnode with multiple links inside
        node = TextNode("This is text with a [link text](http://example.com) link and [another link](http://another.com)", TextType.TEXT)
        # Split it using the link delimiter
        result = split_nodes_link([node])
        # Check the result
        self.assertEqual(len(result), 5)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "link text")
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "http://example.com")
        self.assertEqual(result[2].text, " link and ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "another link")
        self.assertEqual(result[3].text_type, TextType.LINK)
        self.assertEqual(result[3].url, "http://another.com")
        self.assertEqual(result[4].text, "")
        self.assertEqual(result[4].text_type, TextType.TEXT)
    def test_split_nodes_link_with_no_text(self):
        # Create a textnode with no text
        node = TextNode("", TextType.TEXT)
        # Split it using the link delimiter
        result = split_nodes_link([node])
        # Check the result
        self.assertEqual(len(result), 1)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    def test_split_nodes_link_with_no_markdown(self):
        # Create a textnode with no markdown
        node = TextNode("This is just text", TextType.TEXT)
        # Split it using the link delimiter
        result = split_nodes_link([node])
        # Check the result
        self.assertEqual(len(result), 1)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is just text")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    def test_split_nodes_link_with_no_links(self):
        # Create a textnode with no links
        node = TextNode("This is just text", TextType.TEXT)
        # Split it using the link delimiter
        result = split_nodes_link([node])
        # Check the result
        self.assertEqual(len(result), 1)
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is just text")
        self.assertEqual(result[0].text_type, TextType.TEXT)

if __name__ == '__main__':
    unittest.main()