class ZStr():
    def __init__(self, str_base=''):
        self._str_base = str_base

    def __repr__(self):
        return '\'{}\''.format(self._str_base)

    def __str__(self):
        return self._str_base

    def __getitem__(self, index):
        return self._str_base[index]

    def __contains__(self, chars):
        if chars is '':
            return True
        for i in range(len(self._str_base)):
            if chars == self._str_base[i:len(chars) + i]:
                return True
        return False

    def __len__(self):
        return len(self._str_base)

    def __add__(self, obj):
        if type(obj) != str and type(obj) != type(self):
            return
        return ZStr(self._str_base + str(obj))

    def __mul__(self, obj):
        if type(obj) != int:
            return
        return self._str_base * obj


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

def test_2_chars_in_str():
    assert ('to' in str('toto')) == ('to' in ZStr('toto'))

def test_3_chars_in_str():
    assert ('tot' in str('toto')) == ('tot' in ZStr('toto'))

def test_str_chars_in_str():
    assert ('toto' in str('toto')) == ('toto' in ZStr('toto'))

def test_chars_not_in_str():
    assert ('tota' in str('toto')) == ('tota' in ZStr('toto'))

def test_str_longer_in_str():
    assert ('totoo' in str('toto')) == ('totoo' in ZStr('toto'))

def test_len_str():
    assert len('toto')== len(ZStr('toto'))

def test_str_add_str():
    assert str('to' + 'to') == str(ZStr('to') + ZStr('to'))

def test_str_mul_int():
    assert str('to' * 2) == str(ZStr('to') * 2)
