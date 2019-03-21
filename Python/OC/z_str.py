class ZStr():
    def __init__(self, str_base=''):
        self._str_base = ''

    def __repr__(self):
        return '\'\''


def test_basic_repr():
    assert repr(str()) == repr(ZStr())
