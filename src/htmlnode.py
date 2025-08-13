

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplemented)
    
    def props_to_html(self):
        prop_string = ""
        for prop in self.props:
            prop_string+=f' {prop[0]}={prop[1]}'
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
    def __eq__(self, node_to_compare):
        if self.tag == node_to_compare.tag and self.value == node_to_compare.value and self.children == node_to_compare.children and self.props == node_to_compare.props:
            return True
        return False