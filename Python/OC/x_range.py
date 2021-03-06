def x_range(start_stop, stop=None, step=1):
    yielded = 0 if stop is None else start_stop
    ystop = start_stop if stop is None else stop

    while yielded < ystop:
        yield yielded
        yielded += step

def test_basic_range0():
    assert [_ for _ in range(0)] == [_ for _ in x_range(0)]

def test_basic_range1():
    assert [_ for _ in range(1)] == [_ for _ in x_range(1)]

def test_long_range():
    assert [_ for _ in range(100)] == [_ for _ in x_range(100)]

def test_startstop_long_range():
    assert [_ for _ in range(40, 100)] == [_ for _ in x_range(40, 100)]

def test_startstopstep_basic_long_range():
    assert [_ for _ in range(40, 100, 1)] == [_ for _ in x_range(40, 100, 1)]

def test_startstopstep_long_range():
    assert [_ for _ in range(40, 100, 10)] == [_ for _ in x_range(40, 100, 10)]

if __name__ == '__main__':
    pass
