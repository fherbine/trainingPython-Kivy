class ElementBase:
    static = True

    def __init__(self, skin, **kwargs):
        self.skin = skin
        self.collide = kwargs.get('collide', False)
        self._pos = None

    def _set_pos(self, new_pos):
        if new_pos is None:
            self.pos = None

        self.x, self.y = new_pos
        self._pos = new_pos

    def _get_pos(self):
        return self._pos

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

    def make_door(self, collide_elem):
        collide_elem.skin = '.'
        collide_elem.collide = True

    def make_wall(self, collide_elem):
        collide_elem.skin = 'O'
        collide_elem.collide = False

    def copy_element(self, element):
        self.pos = element.pos

    pos = property(_get_pos, _set_pos)


class UserElement(ElementBase):
    def __init__(self, skin):
        super().__init__(skin)
        self.static = False


class WallElement(ElementBase):
    def __init__(self):
        skin = 'O'
        super().__init__(skin)


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
