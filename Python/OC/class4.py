def python_command(cmd, glob=None, loc=None):
    """ python command interpreter """

    if type(cmd) != str:
        print('invalid command: \'{}\''.format(cmd))
        return

    print('$> {}'.format(cmd))
    return eval(cmd, glob, loc)

class Player():
    """ Player class : pedagogic python class """

    def __init__(self, name='fherbine', age=20):
        """ class constructor"""
        self._name = name
        self._age = age

    def __str__(self):
        """ str() format of the class"""
        attrs = [attr for attr in dir(self) if callable(getattr(self, attr))]
        mths = [mth for mth in dir(self) if mth not in attrs]
        return '{name} object with the following attributes: {attrs}, and \
        the following methods {mths}'.format(
            name=self.__class__.__name__,
            attrs=attrs,
            mths=mths,
        )

    def __repr__(self):
        """ Class reprensentation in interpreter """
        return '{name} at {object_id}'.format(
            name=self.__class__.__name__,
            object_id=id(self),
        )

    def _get_name(self):
        """ name attribute getter """
        print('call to name attibute')
        return self._name

    def _set_name(self, name):
        """ name attribute setter """
        print('change name attibute')
        self._name = name

    def __del__(self):
        """ Called method when the object class is suppressed """
        print('"And now the end is near..." F.Sinatra')

    def __getattr__(self, attr):
        """ Called if a called attribute is not existing """
        print('There isn\'t \'{attr}\' attribute'.format(attr=attr))

    def __setattr__(self, attr, value):
        """ Call whenever an attribute is set """
        print('Attribute {attr} set to value {value}'.format(attr=attr, value=value))
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        """ Called method when a attribute is deleted """

        #raise AttributeError('Cannot delete any attributes from class')
        print('{} will be deleted.'.format(attr))
        object.__delattr__(self, attr)


    name = property(_get_name, _set_name)

if __name__ == '__main__':
    p1 = python_command('Player()')
    print(repr(p1))
    print(p1)
    print(python_command('p1.name'))
    p1.name = 'fefe'
    print(python_command('p1.name'))
    del p1
    p2 = Player()
    p2.skills
    p2.age = 5
    p2.skills = 3
    print(python_command('p2.skills'))
    del p2.skills
    p2.skills
