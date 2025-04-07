import unittest
from htmlnode import HTMLNode

class TestTextHTML(unittest.TestCase):
    def test_check(self):
        dict1 = {}
        
        
        dict1["href"] = "http://test1.com"
        dict1["target"] = "__blank"
        
        node = HTMLNode(None, None, None, dict1)
        output = node.props_to_html()
        expected_output = ' href="http://test1.com" target="__blank"'
        self.assertEqual(output, expected_output)
    def test_singleattribute(self): 
        dict2 = {}
        dict2["class"] = "example"
        node2 = HTMLNode(None, None, None, dict2)
        output2 = node2.props_to_html()
        expected_output2 = ' class="example"'
        self.assertEqual(output2, expected_output2)
    def test_empty(self):
        dict3 = {}
        node = HTMLNode(None, None, None, dict3)
        output = node.props_to_html()
        expected_output = ""
        self.assertEqual(output, expected_output)
if __name__ == "__main__":
    unittest.main()