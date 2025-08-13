from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super(ParentNode, self).__init__(tag, None, children, props)
        if self.tag == None:
            raise ValueError("Parent Node requires a tag")
        if self.children == None:
            raise ValueError("Parent Node must have children")
        
    def to_html(self):
        return_string = f'<{self.tag}>'
        for child in self.children:
            return_string+=child.to_html()
        return_string+=f'</{self.tag}>'
        return return_string