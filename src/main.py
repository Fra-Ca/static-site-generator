from textnode import *

def main():
    test_node = TextNode("random text", TextType.LINK, "https://boot.dev")
    print(test_node)
    return test_node

if __name__=="__main__":
    main()