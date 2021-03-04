class Tag:
    types = ['undefined', 'Player', 'Enemy', 'Projectile']

    # Initial tag is a string set to Undefined.
    def __init__(self, tag='undefined'):
        self.tag = tag


