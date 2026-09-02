from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main()-> None:
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    string_node = node.to_html()
    string_result = '<a href="https://www.google.com">Click me!</a>'
    print(string_node)
    

main()



