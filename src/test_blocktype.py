from blocktype import * 
import unittest

class TestBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_heading(self):
        #Test different heading levels
        block1 = "# Heading 1"
        block2 = "## Heading 2"
        block3 = "### Heading 3"
        self.assertEqual(block_to_block_type(block1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block3), BlockType.HEADING)
    def test_code(self):
        block = "```python\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    def test_quote(self):
        block = "> This is a quote\n>Second line of the quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    def test_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    def test_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    #Edge cases
    def test_not_heading(self):
        block = "This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_not_code(self):
        block = "This is not a code block"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_not_quote(self):
        block = "This is not a quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_not_unordered_list(self):
        block = "This is not an unordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_not_ordered_list(self):
        block = "This is not an ordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_empty_block(self):
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_whitespace_block(self):
        block = "   "
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
if __name__ == "__main__":
    unittest.main()
    print("All tests passed!")