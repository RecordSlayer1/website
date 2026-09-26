from enum import Enum
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from splitnodes import text_to_textnodes
from textnode import text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code block'
    QUOTE = 'quote'
    ULIST = 'unordered_list'
    OLIST = 'ordered_list'


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str)-> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        children.append(block_type_to_html_node(block, block_type))
    return ParentNode('div', children)
        
        


def block_type_to_html_node(block: str, block_type: BlockType)-> HTMLNode:
    match block_type:
        case BlockType.PARAGRAPH:
            striped_block = block.replace('\n', ' ')
            children = text_to_children(striped_block)
            return ParentNode('p', children)

        case BlockType.HEADING:
            i = 0
            while block[i] == '#':
                i += 1
            striped_block = block.replace('\n', ' ')
            children = text_to_children(striped_block[i + 1:])
            return ParentNode(f"h{i}", children)

        case BlockType.CODE:
            striped_block = block.removeprefix("```\n").removesuffix("```")
            node = TextNode(striped_block, TextType.CODE)
            return ParentNode('pre', [text_node_to_html_node(node)])
        
        case BlockType.QUOTE:
            sections = block.split('\n')
            striped_sections =[]
            for section in sections:
                striped_sections.append(section.removeprefix('>').strip())
            striped_block = ' '.join(striped_sections)
            children = text_to_children(striped_block)
            return ParentNode('blockquote', children)

        case BlockType.ULIST:
            sections = block.split('\n')
            children = []
            for section in sections:
                striped_section = section.removeprefix('- ')
                section_children = text_to_children(striped_section)
                children.append(ParentNode('li', section_children))
            return ParentNode('ul', children)

        case BlockType.OLIST:
            sections = block.split('\n')
            children = []
            for i in range(len(sections)):
                striped_section = sections[i].removeprefix(f"{i + 1}. ")
                section_children = text_to_children(striped_section)
                children.append(ParentNode('li', section_children))
            return ParentNode('ol', children)
        case _:
            raise ValueError(f'invalid block type: {block_type}')


def text_to_children(text: str)-> list[LeafNode]:
    nodes = text_to_textnodes(text)
    new_nodes = []
    for node in nodes:
        new_nodes.append(text_node_to_html_node(node))
    return new_nodes

def extract_title(markdown: str)-> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith('# '):
            striped_block = block.removeprefix('# ').strip()
            return striped_block
    raise ValueError('no title found')
