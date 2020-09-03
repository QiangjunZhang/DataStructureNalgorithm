import unittest
from DataStructure.pylist import PyList
from DataStructure.hashset import HashSet


class PyListMethods(unittest.TestCase):
    def test_append(self):
        list1 = PyList([1,2,3])
        list1.append(4)
        self.assertEqual(list1.get(0), 1)
        self.assertEqual(list1.get(1), 2)
        self.assertEqual(list1.get(2), 3)
        self.assertEqual(list1.get(3), 4)
        self.assertEqual(list1.get(4), 'Key Error')
        list1.append(5)
        self.assertEqual(list1.get(4), 5)

    def test_len(self):
        list1 = PyList([1, 2, 3])
        list1.append(4)
        self.assertEqual(list1.len(), 4)
        list1.append(5)
        self.assertEqual(list1.len(), 5)
        for _ in range(5):
            list1.append(5)
        self.assertEqual(list1.len(), 10)


class HashSetMethods(unittest.TestCase):
    def test_add(self):
        s = HashSet()
        self.assertEqual(5 in s, False)
        s.add(5)
        self.assertEqual(5 in s, True)
        s.add(6)
        self.assertEqual(6 in s, True)
        s.add(7)
        self.assertEqual(7 in s, True)

    def test_remove(self):
        s = HashSet()
        self.assertEqual(5 in s, False)
        s.add(5)
        s.add(15)
        s.add(6)
        self.assertEqual(5 in s, True)
        self.assertEqual(6 in s, True)
        self.assertEqual(7 in s, False)
        s.remove(5)
        with self.assertRaisesRegex(KeyError, 'Item not in HashSet'):
            s.remove(7)
        self.assertEqual(5 in s, False)


if __name__ == '__main__':
    unittest.main()