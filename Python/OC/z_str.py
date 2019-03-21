class ZStr():
    def __init__(self, str_base=''):
        self._str_base = str_base

    def __repr__(self):
        return '\'{}\''.format(self._str_base)

    def __str__(self):
        return self._str_base

    def __getitem__(self, index):
        return self._str_base[index]

    def __contains__(self, char):
        if char is '':
            return True
        for c in self._str_base:
            if c is char:
                return True
        return False


def test_basic_repr():
    assert repr(str()) == repr(ZStr())

def test_str_repr():
    assert repr(str('toto')) == repr(ZStr('toto'))

def test_basic_str():
    assert str(str()) == str(ZStr())

def test_str_str():
    assert str(str('toto')) == str(ZStr('toto'))

def test_str_index_char():
    assert str('pato')[2] == ZStr('pato')[2]

def test_no_char_in_empty_str():
    assert ('' in str()) == ('' in ZStr())

def test_no_char_in_str():
    assert ('' in str('toto')) == ('' in ZStr('toto'))

def test_one_char_in_str():
    assert ('o' in str('toto')) == ('o' in ZStr('toto'))
