class HTMLNode:
    #props needs to be an dictionary of properties
    #children needs to be a string or list of strings
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        elif type(self.props) != dict:
            print(type(self.props))
            raise Exception("self.props needs to be a dictionary of properties ex. {href: 'www.google.com', target:'_blank'} ")
        html_props_str = ""
        for prop in self.props:
            html_props_str += f' {prop}= "{self.props[prop]}"'
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
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    


class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag specified")
        if self.children == None:
            raise ValueError("no children specified. children arg required")
        children = ""
        for child in self.children:
           children += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        text_node = LeafNode(text_node.text)
        return text_node
    if text_node.text_type == "bold":
        text_node = LeafNode(text_node.text,"b")
        return text_node
    if text_node.text_type == "italic":
        text_node = LeafNode(text_node.text,"i")
        return text_node
    if text_node.text_type == "code":
        text_node = LeafNode(text_node.text,"code")
        return text_node
    if text_node.text_type == "link":
        text_node = LeafNode(text_node.text,"a",{"href": text_node.url})
        return text_node
    if text_node.text_type == "image":
        text_node = LeafNode("","img",{"src": text_node.url, "alt": text_node.text})
        return text_node
    raise Exception("Text type not valid")
    