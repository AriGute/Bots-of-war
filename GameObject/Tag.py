class Tag:
    types = ['undefined']

    # Initial tag is a string set to Undefined.
    # TODO: Add different types to static types string list.
    def __init__(self):
        self.tag = Tag.types[0]


