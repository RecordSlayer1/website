from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] | None = None
        )-> None:
        super().__init__(tag, None, children, props)

    def to_html(self)-> str:
        if self.tag is None:
            raise ValueError('Invalid HTML: missing tag')
        if self.children is None:
            raise ValueError('Invalid HTML: missing children')
        children_node = ''
        for child in self.children:
            children_node += child.to_html()
        if not self.props:
            return f"<{self.tag}>{children_node}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{children_node}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"
