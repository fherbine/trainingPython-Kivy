class ZDict():
    def __repr__(self):
        return '{}'

    def __str__(self):
        return '{}'



def test_dict_str_print():
    assert print(dict()) == print(ZDict())

def test_dict_repr_print():
    assert print(repr(dict())) == print(repr(ZDict()))
