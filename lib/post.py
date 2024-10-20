class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Title:{self.title},Content:{self.content},Post ID:{self.id}"
