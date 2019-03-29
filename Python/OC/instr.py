class InStr():
    """ InStr: just an infinite str """

    def __init__(self, base_string=''):
        self._base_str = base_string

    def __repr__(self):
        return "'{}'".format(self._base_str)

    def __str__(self):
        return '{}'.format(self._base_str)

    def __eq__(self, obj_cmp):
        if type(obj_cmp) != self.__class__:
            return False
        if self._base_str == obj_cmp._base_str:
            return True
        return False

    def __ne__(self, obj_cmp):
        if type(obj_cmp) != self.__class__:
            return True
        if self._base_str == obj_cmp._base_str:
            return False
        return True

    def __getitem__(self, index):
        return self._base_str[index]


def test_basic_repr():
    assert repr(str()) == repr(InStr())

def test_basic_str():
    assert str(str()) == str(InStr())

def test_chars_str_repr():
    assert repr(str('toto')) == repr(InStr('toto'))

def test_chars_str_str():
    assert str(str('toto')) == str(InStr('toto'))

def test_str_int():
    assert str(str(3)) == str(InStr(3))

def test_str_float():
    assert str(str(3.6)) == str(InStr(3.6))

def test_str_list():
    assert str(str(list())) == str(InStr(list()))

def test_str_dict():
    assert str(str(dict())) == str(InStr(dict()))

def test_eq_empty():
    assert bool(str() == str()) == bool(InStr() == InStr())

def test_non_eq_empty():
    assert bool(str('v') == str()) == bool(InStr('v') == InStr())

def test_ne_empty():
    assert bool(str('v') != str()) == bool(InStr('v') != InStr())

def test_non_ne_empty():
    assert bool(str() != str()) == bool(InStr() != InStr())

def test_empty_get_item():
    assert str('z')[-1] == InStr('z')[-1]


if __name__ == '__main__':
    pass
