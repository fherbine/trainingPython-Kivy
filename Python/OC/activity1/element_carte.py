# -*-coding:Utf-8 -*

"""Ce fichier permet de creer un bloc quelconque sur la map."""

class ElementCarte:
    """ElementCarte est la classe parente permettant de définir n'importe quel
    objet sur la carte
    """

    def __init__(self, position, collapsable=True, movable=False):
        """Constructeur on lui passe en argument l'instance, ainsi que
        collapsable, un argument permettant de savoir si l'objet peut se
        superoser à un autre et position"""

        self._collapsable = collapsable
        self._position = position
        self._movable = movable

    @property
    def position(self):
        """Getter de l'attribut postion"""

        return self._position

    @position.setter
    def position(self, position):
        """Setter de l'attribut position."""

        self._position = position

    def __eq__(self, elem_object):
        """Methode eq pour verifier si les posisition des objets sont égales."""

        # On verifie si la classe mere, celle ci est equivalente puisque cette
        # classe n'est pas faite pour être utilisée directement
        # (voir les classes filles ci-dessous).

        self_mothers_class = self.__class__.__bases__
        elem_mothers_class = elem_object.__class__.__bases__

        if not self.mothers_class == elem_mothers_class:
            raise TypeError('Both class should inherit from ElementCarte.')

        # Si c'est les classes héritent de la classe mere ElementCarte,
        # on verifie les positions

        return self.position == elem_object.position

    def __add__(self, elem_object):
        """La methode add, a dans notre cas plus complexité que eq,
        puisque elle peut permettre à la fois d'ajouter une position à un
        Element ou de verifier la colision potentiel entre deux objets.
        """

        self_mothers_class = self.__class__.__bases__
        elem_mothers_class = elem_object.__class__.__bases__

        if self_mothers_class == elem_mothers_class:
            # on retourne True si les deux element sont
            # collapsable (superposale) sinon False
            return (self._collapsable and elem_object._collapsable)

        if (
            type(elem_object) == tuple or type(elem_object) == list
        ) and len(elem_object) == 2 and self._movable:
            # On retourne la position elem_object (tuple ou list) plus la
            # position de notre objet
            return [xy + dxy for xy, dxy in zip(
                self.position,
                elem_object,
            )]
        return False

    def __sub__(self, move):
        """La methode spoeciale sub permet juste de soustraire une position.
        """

        if (
            type(move) == list or type(move) == tuple
        ) and len(move) == 2 and self._movable:
            return [xy + dxy for xy, dxy in zip(self.position, move)]
        else:
            raise TypeError(
                'The first Element should be movable and the second element \
                of the substitution should be either tuple or list'
            )


class Personnage(ElementCarte):
    """Personnage (user) héritant de Element Carte"""

    def __init__(self, position):
        """Constructeur de Personnage prenant en compte la position de ce dernier.
        """

        # fonction super() me permettant de faire appel a la methode init de
        # la classe parente en controllant l'argument movable et position
        super(Personnage, self).__init__(position, movable=True)


class Mur(ElementCarte):
    """Mur héritant de Element Carte"""

    def __init__(self, position):
        """Constructeur de Mur prenant en compte la position de ce dernier.
        """

        # fonction super() me permettant de faire appel a la methode init de
        # la classe parente en controllant l'argument collapsable et position
        super(Mur, self).__init__(position, collapsable=False)


class Porte(ElementCarte):
    """Porte héritant de Element Carte"""

    def __init__(self, position):
        """Constructeur de Porte prenant en compte la position de ce dernier.
        """

        # fonction super() me permettant de faire appel a la methode init de
        # la classe parente en controllant l'argument position
        super(Porte, self).__init__(position)


class Arrivee(ElementCarte):
    """Porte héritant de Element Arrivee"""

    def __init__(self, position):
        """Constructeur de Arrivee prenant en compte la position de ce dernier.
        """

        # fonction super() me permettant de faire appel a la methode init de
        # la classe parente en controllant l'argument position
        super(Arrivee, self).__init__(position)
