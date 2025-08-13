from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD =  "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK =  "link"
    IMAGE = "Image"

class TextNode():
    def __init__(self, text = "", text_type = TextType.TEXT, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node_to_compare):
        if self.text == node_to_compare.text and self.text_type == node_to_compare.text_type and self.url == node_to_compare.url:
            return True
        return False
    
    def __repr__(self):
        return(f'TextNode({self.text}, {self.text_type}, {self.url})')
    
    

    