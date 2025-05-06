import unittest
from markdown_to_html_node import *

def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
def test_header(self):
    md = """
# This is a header
## This is a subheader
### This is a subsubheader
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>This is a header</h1><h2>This is a subheader</h2><h3>This is a subsubheader</h3></div>",
    )
def test_image(self):
    md = """
![alt text](https://example.com/image.png)
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><img src='https://example.com/image.png' alt='alt text'></div>",
    )
def test_link(self):
    md = """
[This is a link](https://example.com)
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><a href='https://example.com'>This is a link</a></div>",
    )
def test_quote(self):
    md = """
> This is a quote
> with multiple lines
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>This is a quote\nwith multiple lines</blockquote></div>",
    )
def test_unordered_list(self):
    md = """
* Item 1
* Item 2
* Item 3
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
    )
def test_ordered_list(self):
    md = """
1. First item
2. Second item
3. Third item
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
    )
def test_nested_lists(self):
    md = """
* Item 1
  * Subitem 1.1
  * Subitem 1.2
* Item 2
  * Subitem 2.1
  * Subitem 2.2
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>Item 1<ul><li>Subitem 1.1</li><li>Subitem 1.2</li></ul></li><li>Item 2<ul><li>Subitem 2.1</li><li>Subitem 2.2</li></ul></li></ul></div>",
    )
def test_nested_lists_with_ordered(self):
    md = """
1. Item 1
  1. Subitem 1.1
  2. Subitem 1.2
2. Item 2
  1. Subitem 2.1
  2. Subitem 2.2
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>Item 1<ol><li>Subitem 1.1</li><li>Subitem 1.2</li></ol></li><li>Item 2<ol><li>Subitem 2.1</li><li>Subitem 2.2</li></ol></li></ol></div>",
    )
def test_nested_lists_with_mixed(self):
    md = """
* Item 1
  1. Subitem 1.1
  * Subitem 1.2
* Item 2
  1. Subitem 2.1
  * Subitem 2.2
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>Item 1<ol><li>Subitem 1.1</li></ol><ul><li>Subitem 1.2</li></ul></li><li>Item 2<ol><li>Subitem 2.1</li></ol><ul><li>Subitem 2.2</li></ul></li></ul></div>",
    )
def test_nested_lists_with_mixed_ordered(self):
    md = """
1. Item 1
  1. Subitem 1.1
  * Subitem 1.2
2. Item 2
  1. Subitem 2.1
  * Subitem 2.2
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>Item 1<ol><li>Subitem 1.1</li></ol><ul><li>Subitem 1.2</li></ul></li><li>Item 2<ol><li>Subitem 2.1</li></ol><ul><li>Subitem 2.2</li></ul></li></ol></div>",
    )
if __name__ == "__main__":
    unittest.main()