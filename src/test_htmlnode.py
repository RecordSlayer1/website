import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_props_to_html_empty(self):
        random_dict = {}
        node = HTMLNode(props=random_dict)
        string = node.props_to_html()
        self.assertEqual('',string)

    def test_props_to_html(self):
        random_dict = {
            "href": "www.nonelink.com",
            "target": "blank++"
        }

        node = HTMLNode(props=random_dict)
        string = node.props_to_html()
        self.assertEqual(f' href="www.nonelink.com" target="blank++"', string)

    def test_repr(self):
        random_dict = {
            'some command': 'some value'
        }
        node = HTMLNode("text", "value", props=random_dict)
        string = "HtmlNode(text, value, children: None, " + "{" + "'some command'" + ": " + "'some value'" + "})"
        self.assertEqual(string, str(node))

        

