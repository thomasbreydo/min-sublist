import min_sublist


def test_min_sublist():
    assert [1, 2, -10] == min_sublist.min_sublist([1, -10, 3])
    assert [1, 5, -12] == min_sublist.min_sublist([1, -10, 3, -4, -1, 3])
    assert [0, 4, -12] == min_sublist.min_sublist([-10, 3, -4, -1, 3])
    assert [0, 3, -10] == min_sublist.min_sublist([0, 0, -10])
    assert [0, 1, 10] == min_sublist.min_sublist([10, 15, 30, 2000])
    assert [0, 3, -9] == min_sublist.min_sublist([-1, -3, -5])
    assert [3, 4, -5] == min_sublist.min_sublist([-1, -3, 6, -5])
    assert [0, 2, -4] == min_sublist.min_sublist([-1, -3, 4, -3])


def test_min_cont_return():
    inp = """-0.42%
0.17%
0.07%
-0.06%
0.37%
-0.07%
-0.02%"""
    inputs = [float(n[:-1]) / 100 for n in inp.strip().split("\n")]
    assert [0, 1, -0.0042] == min_sublist.min_cont_return(inputs)
