from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super(LeafNode, self).__init__(tag, value, None, props)
        if self.value == None:
            raise ValueError("Leaf Node must have a value")
        
    def to_html(self):
        if self.tag == None:
            return rf'{self.value}'
        elif self.props != None:
            return_string = rf"<{self.tag}"
            for prop in self.props:
                return_string+=rf" {prop}={self.props[prop]}"
            return_string +=rf">{self.value}</{self.tag}>"
            return return_string
        else:
            return rf"<{self.tag}>{self.value}</{self.tag}>"

