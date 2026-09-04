import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    

    def test_repr(self):
        child_node1 = LeafNode('a', 'random text')
        child_node2 = LeafNode('a', 'random text 2', {'href': 'www.somelink.com'})
        parent_node = ParentNode('p', [child_node1, child_node2], {'href': 'www.parentlink.com'})
        self.assertEqual(
            parent_node.__repr__(),
            "ParentNode(tag: p, children: [LeafNode(a, random text, None), LeafNode(a, random text 2, {'href': 'www.somelink.com'})], props: {'href': 'www.parentlink.com'})"
        )
    

    def test_child_node_multiple(self):
        child_node1 = LeafNode('h1', 'child_node1', {'child_node1': 'props'})
        child_node2 = LeafNode('h2', 'child_node2', {'child_node2': 'props', 'child_node2': 'props2'})
        parent_node1 = ParentNode('div', [child_node1, child_node2])
        parent_node2 = ParentNode('span', [parent_node1], {'parent_node2': 'props'})
        self.assertEqual(
            parent_node2.to_html(),
            '<span parent_node2="props"><div><h1 child_node1="props">child_node1</h1><h2 child_node2="props2">child_node2</h2></div></span>'
        )


    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

