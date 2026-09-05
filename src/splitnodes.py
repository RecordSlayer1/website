from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if not validate_syntax(old_node.text, delimiter):
            raise ValueError('invalidid syntax')
        
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

