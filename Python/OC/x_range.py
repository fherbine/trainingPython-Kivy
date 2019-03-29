def x_range(start_stop, stop=None, step=None):
    yielded = 0
    if start_stop:
        while yielded < start_stop:
            yield yielded
            yielded += 1

def test_basic_range0():
    assert [_ for _ in range(0)] == [_ for _ in x_range(0)]

def test_basic_range1():
    assert [_ for _ in range(1)] == [_ for _ in x_range(1)]

def test_long_range():
    assert [_ for _ in range(100)] == [_ for _ in x_range(100)]

if __name__ == '__main__':
    pass
