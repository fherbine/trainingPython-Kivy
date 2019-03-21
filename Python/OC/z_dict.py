class ZDict():
    """ A sort of dict() """

    def __init__(self, **kwargs):
        """ Class's constructor """
        self._dict_content = kwargs

    def __repr__(self):
        """ Class representation """
        return str(self._dict_content)

    def __str__(self):
        """ Called when class is converted to str() """
        return str(self._dict_content)

    def __getitem__(self, index):
        """ Return item object from index """
        return self._dict_content[index]

    def __setitem__(self, index, value):
        """ Set the object at index `index` to `value` object """

        self._dict_content[index] = value


def test_dict_str_print():
    assert print(dict()) == print(ZDict())

def test_dict_repr_print():
    assert print(repr(dict())) == print(repr(ZDict()))

def test_dict_one_elem_at_init_str():
    assert str(dict(key='value')) == str(ZDict(key='value'))

def test_dict_several_elems_at_init_str():
    assert str(dict(key='value', key2='v2')) == str(ZDict(key='value', key2='v2'))

def test_add_one_item_getkey_convert_str():
    a = dict(key='val')
    b = ZDict(key='val')
    assert a['key'] == b['key']

def test_add_several_item_getkey_convert_str():
    a = dict(key='val', v2=0, v3=False)
    b = ZDict(key='val', v2=0, v3=False)
    assert str(a['key'] + str(a['v3'])) == str(b['key'] + str(b['v3']))
