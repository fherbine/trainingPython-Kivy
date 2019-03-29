class InStr():
    """ InStr: just an infinite str """

    def __init__(self, base_string=''):
        self.base_str = base_string

    def __repr__(self):
        return "'{}'".format(self.base_str)

    def __str__(self):
        return '{}'.format(self.base_str)


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

if __name__ == '__main__':
    pass
