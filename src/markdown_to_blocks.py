

def markdown_to_blocks(markdown_text):
    """
    Convert markdown text to a list of blocks.
    """
    # Convert markdown text into blocks based on blank lines
    raw_blocks = markdown_text.split('\n\n')

    #Strip each block and filter out empty ones
    blocks = [block.strip() for block in raw_blocks if block.strip()]

    

    return blocks