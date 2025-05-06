import unittest
from extract_markdown_images import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_images(self):
        text = "![alt text](image.png)"
        expected = [("alt text", "image.png")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)
    def test_extract_images_with_text(self):
        text = "![alt text](image.png) and some text"
        expected = [("alt text", "image.png")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)
    def test_extract_images_with_multiple(self):
        text = "![alt text](image.png) and ![another image](another.png)"
        expected = [("alt text", "image.png"), ("another image", "another.png")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)
    def test_extract_images_with_no_alt_text(self):
        text = "![](image.png)"
        expected = [("", "image.png")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)
    def test_extract_images_with_no_image(self):
        text = "![alt text]()"
        expected = [("alt text", "")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)
    def test_extract_images_with_empty_string(self):
        text = ""
        expected = []
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)
    def test_extract_images_with_no_markdown(self):
        text = "This is just text"
        expected = []
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)
    def test_extract_links(self):
        text = "[link text](http://example.com)"
        expected = [("link text", "http://example.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)
    def test_extract_links_with_text(self):
        text = "[link text](http://example.com) and some text"
        expected = [("link text", "http://example.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)
    def test_extract_links_with_multiple(self):
        text = "[link text](http://example.com) and [another link](http://another.com)"
        expected = [("link text", "http://example.com"), ("another link", "http://another.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)
    def test_extract_links_with_no_text(self):
        text = "[](http://example.com)"
        expected = [("", "http://example.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
# test_extract_markdown_images.py
# This file contains unit tests for the extract_markdown_images and extract_markdown_links functions.