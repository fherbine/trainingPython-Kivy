class HumanBeing():
    """ Will devocated to procrastinate """

    def __init__(self, name='toto'):
        """ Class constructor """
        self._name = name

    def _get_name(self):
        """ name attribute getter """
        return self._name

    def _set_name(self, value):
        """ setter of the name attribute """
        self._name = value

    def __repr__(self):
        """ Class representation """
        return '{} at {}'.format(self.__class__.__name__, id(self))

    def __str__(self):
        """ Class's str() version """
        attrs = [attr for attr in dir(self) if callable(getattr(self, attr))]
        mths = [mth for mth in dir(self) if mth not in attrs]
        return '{cls_name} contains the following attributes: {attrs} \
        and methods {meths}'.format(
            cls_name=self.__class__.__name__,
            attrs=attrs,
            meths=mths,
        )

    def __getattr__(self, attr):
        """ Called if attr is not find (undefined at runtime) """

        print('{attr} is undefined !'.format(attr=attr))
        object.__setattr__(self, attr, None)
        print('{attr} is now set with the value \'{val}\''.format(
            attr=attr,
            val=getattr(self, attr)
        ))

    def __setattr__(self, attr, value):
        """ Called when an attribute is set """
        print('{attr} will be set with the value {val}'.format(
            attr=attr,
            val=value,
        ))
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        """ Called when an attribute is deleted """
        print('{attr} will be deleted'.format(attr=attr))
        object.__delattr__(self, attr)

    name = property(_get_name, _set_name)

if __name__ == '__main__':
    eval('HumanBeing()')
    toto = HumanBeing()
    print(toto)
    print(toto.name)
    print(toto.size)
    print(toto.size)
    del toto.size
