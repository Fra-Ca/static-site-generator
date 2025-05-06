from htmlnode import *
from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from textnode import TextType
from textnode import TextNode
from text_to_textnodes import text_to_textnodes
from split_nodes import split_nodes_delimiter
from split_nodes_images import split_nodes_image, split_nodes_link
from extract_markdown_images import extract_markdown_images, extract_markdown_links

def markdown_to_html_node(markdown):
    #Converts a full markdown document to a single parent HTMLNode
    #Create the parent div node
    parent = HTMLNode("div")

    #Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    #Process each block
    for block in blocks:
        #Determine the block type
        block_type = block_to_block_type(block)
        #Create the appropriate HTMLNode based on the block type
        if block_type == BlockType.PARAGRAPH:
            block_node = create_paragraph_node(block)
        elif block_type == BlockType.HEADER:
            block_node = create_header_node(block)
        elif block_type == BlockType.IMAGE:
            block_node = create_image_node(block)
        elif block_type == BlockType.LINK:
            block_node = create_link_node(block)
        elif block_type == BlockType.QUOTE:
            block_node = create_quote_node(block)
        elif block_type == BlockType.CODE:
            block_node = create_code_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            block_node = create_unordered_list_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            block_node = create_ordered_list_node(block)
        else:
            raise ValueError(f"Unknown block type: {block_type}")

        parent.children.append(block_node)
    return parent

def create_paragraph_node(block):
    #Create a paragraph node
    children = text_to_children(block)
    return HTMLNode(tag='p', children=children)
def create_header_node(block):
    #Count the number of # at the beginning to determine the header level
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    #Remove the #s and any leading space
    content = block[level:].lstrip()

    children = text_to_children(content)
    return HTMLNode(tag=f'h{level}', children=children)

def create_image_node(block):
    #Extract the URL and alt text from the block
    url = block.split('](')[1].split(')')[0]
    alt_text = block.split('[')[1].split(']')[0]
    props = {"src": url, "alt": alt_text}
    return LeafNode(tag='img', value=None, props=props)
def create_link_node(block):
    #Extract the URL and text from the block
    url = block.split('](')[1].split(')')[0]
    text = block.split('[')[1].split(']')[0]
    props = {"href": url}
    return LeafNode(tag='a', value=text, props=props)
def create_quote_node(block):
    #Remove the > and any leading space
    content = block[1:].lstrip()
    children = text_to_children(content)
    return HTMLNode(tag='blockquote', children=children)
def create_code_node(block):
    #Strip the ``` from beginning and end
    code_content = block.strip('`').strip()
    
    #For code blocks, we don't parse inline markdown
    text_node = TextNode(code_content, TextType.TEXT)
    code_html_node = text_node_to_html_node(text_node)

    pre_node = HTMLNode(tag='pre', children=[code_html_node])
    return pre_node
def create_unordered_list_node(block):
    #Split the block into lines and process each as a list item
    lines = block.split('\n')
    list_items = []

    for line in lines:
        if line.strip().startswith('* '):
            #Remove the * and create the list item
            content = line.strip()[2:] #Remove "* " and process the rest
            children = text_to_children(content)
            list_item = HTMLNode(tag='li', children=children)
            list_items.append(list_item)
    return HTMLNode(tag='ul', children=list_items)
def create_ordered_list_node(block):
    #Similar to unordered list but for numbered items
    lines = block.split('\n')
    list_items = []
    for line in lines:
        #Check for numbered items like "1. "
        if line.strip() and line.strip()[0].isdigit() and '. ' in line:
            #Remove the "1. " and process the rest
            content = line.strip().split('. ', 1)[1]
            children = text_to_children(content)
            list_item = HTMLNode(tag='li', children=children)
            list_items.append(list_item)
    return HTMLNode(tag='ol', children=list_items)

def text_to_children(text):
    #Convert the text to a list of TextNode objects with proper types
    text_nodes = text_to_textnodes(text)

    #Convert each TextNode to an HTMLNode
    html_nodes = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes


