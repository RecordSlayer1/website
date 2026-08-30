from textnode import TextNode, TextType

def main()-> None:
    node1 = TextNode('unknow string by me', TextType.BOLD_TEXT, 'http/nonsense')
    node2 = TextNode('unknow string by me', TextType.BOLD_TEXT, 'http/nonsense')
    node3 = TextNode('unknow string by me', TextType.TEXT, 'http/nonsense')
    print(node1 == node2)
    print(node1 == node3)
    print(node1)
    print(node3)
main()



