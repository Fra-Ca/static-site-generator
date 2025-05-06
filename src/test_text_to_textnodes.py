from text_to_textnodes import *
import unittest

def test_text_to_textnodes():
    # Test case 1: Basic text
    text = "This is a simple text."
    expected_output = [TextNode(text, TextType.TEXT)]
    assert text_to_textnodes(text) == expected_output

    # Test case 2: Bold text
    text = "This is **bold** text."
    expected_output = [
        TextNode("This is ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text.", TextType.TEXT)
    ]
    assert text_to_textnodes(text) == expected_output

    # Test case 3: Italic text
    text = "This is _italic_ text."
    expected_output = [
        TextNode("This is ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" text.", TextType.TEXT)
    ]
    assert text_to_textnodes(text) == expected_output

    # Test case 4: Code text
    text = "This is `code` text."
    expected_output = [
        TextNode("This is ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" text.", TextType.TEXT)
    ]
    assert text_to_textnodes(text) == expected_output

if __name__ == "__main__":
    test_text_to_textnodes()
    print("All tests passed!")
# This code is a test suite for the text_to_textnodes function, which converts text into a list of TextNode objects with different text types.