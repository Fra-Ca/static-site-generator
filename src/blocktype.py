from enum import Enum

class BlockType(Enum):

    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def block_to_block_type(block):
    """
    Convert a block to its corresponding BlockType.
    """
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    #Check for quote blocks
    lines= block.split("\n")
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    #Check for unordered and ordered lists 
    is_unordered_list = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    expected_num =1
    is_ordered_list = True
    for line in lines:
        if not line.startswith(f"{expected_num}. "):
            is_ordered_list = False
            break
        expected_num += 1
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH