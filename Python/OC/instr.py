class InStr():
    """ InStr: just an infinite str """

    def __repr__(self):
        return "''"

    def __str__(self):
        return ''


def test_basic_repr():
    assert repr(str()) == repr(InStr())

def test_basic_str():
    assert str(str()) == str(InStr())

if __name__ == '__main__':
    pass
