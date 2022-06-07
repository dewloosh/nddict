# -*- coding: utf-8 -*-
import unittest
from copy import copy, deepcopy

from nddict import DeepDict


class TestMain(unittest.TestCase):

    def test_lib_basic(self):
        """
        Qualitative test on basic usage of a DeepDict.
        """
        data = DeepDict()
        data['a', 'b', 'c'] = 1
        f = data.containers
        assert [c.key for c in f(inclusive=True, deep=True)] == [
            None, 'a', 'b']
        assert [c.key for c in f(inclusive=True, deep=False)] == [None, 'a']
        assert [c.key for c in f(inclusive=False, deep=True)] == ['a', 'b']
        assert [c.key for c in f(inclusive=False, deep=False)] == ['a']
        assert data['a', 'b'].depth == 2
        assert data['a', 'b'].key == 'b'
        assert data.is_root() is True
        assert data['a', 'b'].is_root() is False
        assert data['a', 'b'].parent == data['a']
        assert data['a', 'b'].root() == data

        # lock test
        has_error = False
        data.lock()
        assert data.locked
        try:
            data['a', 'b', 'd'] = 2
        except:
            has_error = True
        finally:
            assert has_error
        data.unlock()
        assert not data.locked
        data.locked = False
        has_error = False
        try:
            data['a', 'b', 'd'] = 2
        except:
            has_error = True  # pragma: no cover
        finally:
            assert not has_error

        # try indexing
        data['a']['b']['e'] = 3
        assert data['a', 'b', 'e'] == 3
        
        # other stuff
        data['a', 'b'].root()
        data.__repr__()
        
        #copy(data)
        #deepcopy(data)
        list(data.values())
        list(data.values(deep=True))
        list(data.values(deep=True, return_address=True))
        list(data.keys())
        list(data.keys(deep=True))
        list(data.keys(deep=True, return_address=True))
        list(data.items())
        list(data.items(deep=True))
        list(data.items(deep=True, return_address=True))
        data['_a', '_b', '_e']
        data['_a', '_b', '__e']

    def test_lib_compliance(self):
        """
        Tests to assure that a `DeepDict` works the same way as a `dict`.
        """
        data1 = DeepDict(a=1, b=dict(c=2, d=3))
        data2 = dict(a=1, b=dict(c=2, d=3))
        assert data1 == data2
        assert list(data1.keys()) == list(data1.keys())
        assert list(data1.values()) == list(data1.values())
            
                  
if __name__ == "__main__":
    unittest.main()  # pragma: no cover
