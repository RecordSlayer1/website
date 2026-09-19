from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from splitnodes import split_nodes_image, text_to_textnodes
from markdown_blocks import block_type_to_html_node, BlockType, markdown_to_blocks

def main()-> None:
    md = '''
1. item1
2. item2
3. item3
'''
    markdown = markdown_to_blocks(md)
    node = block_type_to_html_node(markdown[0], BlockType.OLIST)
    print(node.to_html())

main()



