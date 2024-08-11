class HTMLNode:
    #props needs to be an dictionary of properties
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if type(self.props) != dict:
            print(type(self.props))
            raise Exception("self.props needs to be a dictionary of properties ex. {href: 'www.google.com', target:'_blank'} ")
        html_props_str = ""
        for prop in self.props:
            html_props_str += f' {prop}= "{self.props[prop]}" '
        return html_props_str

    def __repr__(self) -> str:
        return f"tag={self.tag} value={self.value} children={self.children} props={self.props}"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag,None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    


   
