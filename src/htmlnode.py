class HTMLNode():
    def __init__(
        self,
        tag: None | str = None,
        value : None | str = None,
        children: None | list["HTMLNode"] = None,
        props: None | dict[str,str] = None
        )-> None:

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self)-> str:
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self)-> str:
        prop_str = ''
        for prop in self.props:
            prop_str +=' ' + prop + '=' + '"' +  self.props[prop] + '"'

        return prop_str

    def __repr__(self)-> None:
        return f"HtmlNode({self.tag}, {self.value}, children: {self.children}, {self.props}"



