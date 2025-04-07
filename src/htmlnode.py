from textnode import TextType
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if not self.props:
            return ""  # No props? Return an empty string.
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    def __repr__(self):
        return f"Tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if self.value is None and self.tag != "img":
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        props = self.props_to_html()
        if self.tag == "img":
            return f"<{self.tag}{props}>"
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        return f"<{self.tag}{self.props_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
    
def text_node_to_html_node(text_node):
    text_type_map = {
        TextType.TEXT: (None, lambda node: None),
        TextType.BOLD: ("b", lambda node: None),
        TextType.ITALIC: ("i", lambda node: None),
        TextType.CODE: ("code", lambda node: None),
        TextType.LINK: ("a", lambda node: {"href": node.url}),
        TextType.IMAGE: ("img", lambda node: {"src": node.url, "alt": node.alt_text}),    
    }
    tag, props_function = text_type_map.get(text_node.text_type, (None, None))
    if tag is None and props_function is None:
        raise ValueError(f"Unknown TextType: {text_node.text_type}")
    props = props_function(text_node)
    return LeafNode(tag, text_node.text, props)
