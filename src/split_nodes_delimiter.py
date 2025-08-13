from textnode import TextNode, TextType
from leafnode import LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    delimiter_count = 0
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            break
        for i in range(0, len(node.text)):
            if node.text[i] == delimiter:
                delimiter_count+=1
        if delimiter_count % 2 != 0:
            raise Exception("Unmatched delimiters")
        delimited_text = node.text.split(delimiter)
        is_text_type = False
        for segment in delimited_text:
            if is_text_type:
                new_node = TextNode(segment, text_type)
                is_text_type = False
            else:
                new_node = TextNode(segment, TextType.TEXT)
                is_text_type = True
            new_nodes.append(new_node)
    return new_nodes         

        