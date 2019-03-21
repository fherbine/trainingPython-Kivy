class ZStr():
    def __init__(self, str_base=''):
        self._str_base = str_base

    def __repr__(self):
        return '\'{}\''.format(self._str_base)


def test_basic_repr():
    assert repr(str()) == repr(ZStr())

def test_str_repr():
    assert repr(str('toto')) == repr(ZStr('toto'))
