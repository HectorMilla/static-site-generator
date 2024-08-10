
class Textnode:
    def __init__(self, text, text_type,url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, text_node2):
        if self.text == text_node2.text and self.text_type == text_node2.text_type and self.url == text_node2.url:
            return True