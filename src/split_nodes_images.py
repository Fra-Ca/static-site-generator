from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links
import re

def split_nodes_image(old_nodes):
    new_nodes = []

    #Only process the text nodes
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
    #Extract all images from the text
        images = extract_markdown_images(node.text)

    #If no images found, just add the original node
        if not images:
            new_nodes.append(node)
            continue
    #Otherwise start splitting the text
        remaining_text = node.text

        for image_alt, image_url in images:
            #Split the text at the first occurrence of the image
            image_markwdown = f"![{image_alt}]({image_url})"
            parts = remaining_text.split(image_markwdown, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                #Add the image node
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

                #Update remaining text
            if len(parts)>1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

                #Add any remaining text after all images
        
        new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
    
def split_nodes_link(old_nodes):
    new_nodes = []

    #Only process the text nodes
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
    #Extract all links from the text
        links = extract_markdown_links(node.text)

    #If no links found, just add the original node
        if not links:
            new_nodes.append(node)
            continue
    #Otherwise start splitting the text
        remaining_text = node.text

        for link_text, link_url in links:
            #Split the text at the first occurrence of the link
            link_markwdown = f"[{link_text}]({link_url})"
            parts = remaining_text.split(link_markwdown, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                #Add the link node
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

                #Update remaining text
            if len(parts)>1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

                #Add any remaining text after all links
        
        new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes    