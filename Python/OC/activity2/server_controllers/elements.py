class ElementBase:
    """Classe mère de toutes les classe element de carte."""

    static = True

    def __init__(self, skin, **kwargs):
        self.skin = skin
        self.collide = kwargs.get('collide', False)
        self._pos = None

    def _set_pos(self, new_pos):
        """Setter de la propriété `pos`"""
        if new_pos is None:
            self.pos = None

        self.x, self.y = new_pos
        self._pos = new_pos

    def _get_pos(self):
        """Getter de la propriété `pos`"""
        return self._pos

    def move_up(self):
        """Specifique aux élément non-statiques.

        effectue un mouvement vers le haut.
        """
        if self.static:
            return

        self.y -= 1
        self._update_pos_from_xy()

    def move_down(self):
        """Specifique aux élément non-statiques.

        effectue un mouvement vers le bas.
        """
        if self.static:
            return

        self.y += 1
        self._update_pos_from_xy()

    def move_left(self):
        """Specifique aux élément non-statiques.

        effectue un mouvement vers la gauche.
        """
        if self.static:
            return

        self.x -= 1
        self._update_pos_from_xy()

    def move_right(self):
        """Specifique aux élément non-statiques.

        effectue un mouvement vers la droite.
        """
        if self.static:
            return

        self.x += 1
        self._update_pos_from_xy()

    def make_door(self, collide_elem):
        """Transformation d'un mur en porte."""
        collide_elem.skin = '.'
        collide_elem.collide = True

    def make_wall(self, collide_elem):
        """Transformation d'une porte en mur."""
        collide_elem.skin = 'O'
        collide_elem.collide = False

    def copy_element(self, element):
        """Copie d'un autre element basé sur ElementBase."""
        self.pos = element.pos

    def _update_pos_from_xy(self):
        self.pos = (self.x, self.y)

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
