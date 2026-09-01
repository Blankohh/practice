from two_sum import has_pair_sum


def test_found():
    assert has_pair_sum([1, 2, 3, 4], 5) is True


def test_not_found():
    assert has_pair_sum([1, 2, 3, 4], 9) is False


def test_empty():
    assert has_pair_sum([], 1) is False


def test_single():
    assert has_pair_sum([2], 4) is False


def test_two_ones():
    assert has_pair_sum([1, 1, 2, 3], 2) is True
