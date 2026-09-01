from selection_sort import selection_sort


def test_empty():
    assert selection_sort([]) == []


def test_single():
    assert selection_sort([5]) == [5]


def test_normal():
    assert selection_sort([3, 1, 2]) == [1, 2, 3]


def test_duplicates():
    assert selection_sort([4, 2, 4, 1]) == [1, 2, 4, 4]


def test_does_not_mutate_input():
    nums = [3, 1, 2]
    selection_sort(nums)
    assert nums == [3, 1, 2]
