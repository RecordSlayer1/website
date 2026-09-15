import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if not validate_syntax(old_node.text, delimiter):
            raise ValueError('invalid syntax')
        
        split_nodes = []
        sections = old_node.text.split(delimiter)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def validate_syntax(text: str, delimiter: str):
    total = 0
    for symbol in text:
        if symbol == delimiter:
            total += 1
    return total % 2 == 0


def extract_markdown_images(text: str)-> list[tuple[str, str]]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text: str)-> list[tuple[str, str]]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = [] 
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        list_of_markdown_images = extract_markdown_images(old_node.text)
        if len(list_of_markdown_images) == 0:
            new_nodes.append(old_node)
            continue

        for mardown_image in list_of_markdown_images:
            image_alt, image_url = mardown_image
            seperation = text.split(f"![{image_alt}]({image_url})")
            if len(seperation) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if seperation[0] != "":
                new_nodes.append(TextNode(seperation[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            text = seperation[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = [] 
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        list_of_markdown_links = extract_markdown_links(text)
        if len(list_of_markdown_links) == 0:
            new_nodes.append(old_node)
            continue

        for mardown_link in list_of_markdown_links:
            link_anker, link_url = mardown_link
            seperation = text.split(f"[{link_anker}]({link_url})")
            if len(seperation) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if seperation[0] != "":
                new_nodes.append(TextNode(seperation[0], TextType.TEXT))
            new_nodes.append(TextNode(link_anker, TextType.LINK, link_url))
            text = seperation[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))  
    return new_nodes


def text_to_textnodes(text: str)-> list[TextNode]:
    node = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(node, '**', TextType.BOLD)
    italic = split_nodes_delimiter(bold, '_', TextType.ITALIC)
    code = split_nodes_delimiter(italic, '`', TextType.CODE)
    image = split_nodes_image(code)
    link = split_nodes_link(image)
    return link


