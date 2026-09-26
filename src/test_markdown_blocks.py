import unittest

from markdown_blocks import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    extract_title
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
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_extract_tile(self):
        title = extract_title('# Hello world   ')
        self.assertEqual(title, 'Hello world')

    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

- and
- a
- list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception:
            pass

if __name__ == "__main__":
    unittest.main()

