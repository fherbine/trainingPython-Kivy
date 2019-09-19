class ElementBase:
    static = True

    def __init__(self, skin, **kwargs):
        self.skin = skin
        self.collide = kwargs.get('collide', False)
        self.pos = None

    def _set_pos(self, new_pos):
        self.x, self.y = pos
        self.pos = pos

    def _get_pos(self):
        return self.pos

    def move_up(self):
        if static:
            return

        self.y -= 1

    def move_down(self):
        if static:
            return

        self.y += 1

    def move_left(self):
        if static:
            return

        self.x -= 1

    def move_right(self):
        if static:
            return

        self.x += 1

    def copy_element(self, element):
        self.pos = element.pos

    pos = property(_get_pos, _set_pos)


class UserElement(ElementBase):
    def __init__(self, skin, pos):
        super().__init__(skin, pos)


class WallElement(ElementBase):
    def __init__(self, pos):
        skin = 'O'
        super().__init__(skin, pos)


class DoorElement(ElementBase):
    def __init__(self):
        skin = '.'
        super().__init__(skin, collide=True)


class EmptyElement(ElementBase):
    def __init__(self):
        skin = ' '
        super().__init__(skin, collide=True)


class ArrivalElement(ElementBase):
    def __init__(self):
        skin = 'U'
        super().__init__(skin, collide=True)
