from markdown_to_blocks import *
import unittest

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        # Test case 1: Basic markdown
        markdown = "This is a simple text."
        expected_output = ["This is a simple text."]
        self.assertEqual(markdown_to_blocks(markdown), expected_output)

        # Test case 2: Multiple paragraphs
        markdown = "This is the first paragraph.\n\nThis is the second paragraph."
        expected_output = ["This is the first paragraph.", "This is the second paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected_output)

        # Test case 3: Extra newlines
        markdown = "This is a paragraph.\n\n\nThis is another paragraph."
        expected_output = ["This is a paragraph.", "This is another paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected_output)
        # Test case 4: Leading and trailing newlines
        markdown = "\n\nThis is a paragraph.\n\n"
        expected_output = ["This is a paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected_output)
        # Test case 5: Empty string
        markdown = ""
        expected_output = []
        self.assertEqual(markdown_to_blocks(markdown), expected_output)
        # Test case 6: Only newlines
        markdown = "\n\n\n"
        expected_output = []
        self.assertEqual(markdown_to_blocks(markdown), expected_output)
        # Test case 7: Mixed content
        markdown = "This is a paragraph.\n\nThis is another paragraph.\n\n\nThis is the third paragraph."

    if __name__ == "__main__":
        unittest.main()
        print("All tests passed!")