from first_index import first_index

def test_repeated():
        assert first_index([1,2,2,2,3],2) == 1

def test_not_found():
        assert first_index([1,2,3],4) == -1

def test_all_same():
        assert first_index([2,2,2],2) == 0

def test_single():
        assert first_index([5],5) == 0

def test_empty():
        assert first_index([],1) == -1
