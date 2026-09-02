from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: str | None = None )-> None:
        super().__init__(tag, value, None, props)

    def to_html(self)-> str:
        if self.value is None:
            raise ValueError ("invalid HTML: no value")
        elif not self.tag:
            return self.value
        elif not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self)-> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"



