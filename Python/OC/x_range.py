def x_range(start_stop, stop=None, step=None):
    if start_stop:
        yield 0

def test_basic_range0():
    assert [_ for _ in range(0)] == [_ for _ in x_range(0)]

def test_basic_range1():
    assert [_ for _ in range(1)] == [_ for _ in x_range(1)]

if __name__ == '__main__':
    pass
