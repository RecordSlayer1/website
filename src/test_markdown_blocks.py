import unittest

from markdown_blocks import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node
    )


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        block = block_to_block_type('#### This is heading')
        self.assertEqual(block, BlockType.HEADING)

    def test_block_to_block_type_heading_other(self):
        block = block_to_block_type('###### This is heading too')
        self.assertEqual(block, BlockType.HEADING)
    
    def test_block_to_block_type_code(self):
        block = block_to_block_type("```\nThis is code block\n```")
        self.assertEqual(block, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = block_to_block_type('>This is quote')
        self.assertEqual(block, BlockType.QUOTE)
    
    def test_block_to_block_type_paragraph(self):
        block = block_to_block_type('This is just paragraph\nwith new line in middle')
        self.assertEqual(block, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_unordered_list(self):
        block = block_to_block_type('- This is unordered list\n- item1\n- item2\n- item3')
        self.assertEqual(block, BlockType.ULIST)
        
    def test_block_to_block_type_ordered_list(self):
        block = block_to_block_type('1. ordered list\n2. item1\n3. item3')
        self.assertEqual(block, BlockType.OLIST)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
if __name__ == "__main__":
    unittest.main()

