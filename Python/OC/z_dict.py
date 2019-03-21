class ZDict():
    """ A sort of dict() """

    def __init__(self, **kwargs):
        self._dict_content = kwargs

    def _get_dict_content(self):
        return self._dict_content

    def _set_dict_content(self, value):
        self._dict_content = value

    def __repr__(self):
        return str(self.dict_content)

    def __str__(self):
        return str(self.dict_content)

    dict_content = property(_get_dict_content, _set_dict_content)


def test_dict_str_print():
    assert print(dict()) == print(ZDict())

def test_dict_repr_print():
    assert print(repr(dict())) == print(repr(ZDict()))

def test_dict_one_elem_at_init_str():
    assert str(dict(key='value')) == str(ZDict(key='value'))

def test_dict_several_elems_at_init_str():
    assert str(dict(key='value', key2='v2')) == str(ZDict(key='value', key2='v2'))
