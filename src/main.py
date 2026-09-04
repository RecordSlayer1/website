from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main()-> None:
    child_node1 = LeafNode('h1', 'child_node1', {'child_node1': 'props'})
    child_node2 = LeafNode('h2', 'child_node2', {'child_node2': 'props', 'child_node2': 'props2'})
    parent_node1 = ParentNode('div', [child_node1, child_node2])
    parent_node2 = ParentNode('span', [parent_node1], {'parent_node2': 'props'})
    print(parent_node2.to_html())

main()



