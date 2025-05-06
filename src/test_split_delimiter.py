import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_text_with_code(self):
        #Create a textnode with some code inside
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        #Split it using the backtick delimiter for code
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        #Check the result
        self.assertEqual(len(result), 3)
        #Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code block")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    def test_split_text_with_code_and_other_delimiter(self):
        #Create a textnode with some code inside and other delimiters
        node = TextNode("This is text with a `code block` word and some *bold* text", TextType.TEXT)
        #Split it using the backtick delimiter for code and asterisk for bold
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        result = split_nodes_delimiter(result, "*", TextType.BOLD)
        #Check the result
        self.assertEqual(len(result), 5)
        #Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code block")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " word and some ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "bold")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[4].text, " text")
        self.assertEqual(result[4].text_type, TextType.TEXT)
    def test_split_text_with_no_code(self):
        #Create a textnode with no code inside
        node = TextNode("This is just text", TextType.TEXT)
        #Split it using the backtick delimiter for code
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        #Check the result
        self.assertEqual(len(result), 1)
        #Check the content and type of each node
        self.assertEqual(result[0].text, "This is just text")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    def test_split_text_with_empty_string(self):
        #Create a textnode with an empty string
        node = TextNode("", TextType.TEXT)
        #Split it using the backtick delimiter for code
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        #Check the result
        self.assertEqual(len(result), 1)
        #Check the content and type of each node
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    def test_split_text_with_multiple_delimiters(self):
        #Create a textnode with multiple delimiters
        node = TextNode("This is text with a `code block` and *bold* text", TextType.TEXT)
        #Split it using the backtick delimiter for code and asterisk for bold
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        result = split_nodes_delimiter(result, "*", TextType.BOLD)
        #Check the result
        self.assertEqual(len(result), 5)
        #Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code block")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "bold")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[4].text, " text")
        self.assertEqual(result[4].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()