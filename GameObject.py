from Tag import Tag
import Transform

class GameObject:

    def __init__(self, name='unnamed', id=0):
        self.name = name
        self.tag = Tag()
        self.transform = Transform()
