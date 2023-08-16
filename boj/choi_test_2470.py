import unittest
import sys
from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location("choi", "boj/choi.2470.py")
if spec is None:
    exit(2)
choi = module_from_spec(spec)
sys.modules["choi"] = choi
spec.loader.exec_module(choi)


class Test(unittest.TestCase):
    def test1(self):
        liquids = [-3, -1, 1, 10]
        answer = (-1, 1)
        self.assertEqual(answer, choi.solve(liquids))

    def test2(self):
        liquids = [-4, -1, 4, 6]
        answer = (-4, 4)
        self.assertEqual(answer, choi.solve(liquids))

    def test3(self):
        liquids = [-2, 4, -99, -1, 98]
        answer = (-99, 98)
        self.assertEqual(answer, choi.solve(liquids))

    def test4(self):
        liquids = [-100, -90, 0, 90, 130, 130, 130, 130, 130]
        answer = (-90, 90)
        self.assertEqual(answer, choi.solve(liquids))

    def test5(self):
        liquids = [500, 501]
        answer = (500, 501)
        self.assertEqual(answer, choi.solve(liquids))

    def test6(self):
        liquids = [-999, 1, 2]
        answer = (1, 2)
        self.assertEqual(answer, choi.solve(liquids))

    def test7(self):
        liquids = [-1000000000, -999999999, 333333333, 333333334]
        answer = (-999999999, 333333334)
        self.assertEqual(answer, choi.solve(liquids))

    def test8(self):
        liquids = [-1000000000, -999999999, 1]
        answer = (-999999999, 1)
        self.assertEqual(answer, choi.solve(liquids))

    def test9(self):
        liquids = [1000000000, 999999999]
        answer = (999999999, 1000000000)
        self.assertEqual(answer, choi.solve(liquids))

    def test_timeout1(self):
        n = 100000
        liquids = [i - 100000000 for i in range(n // 2)]
        liquids += [i + 200000000 for i in range(n // 2)]
        choi.solve(liquids)

    def test_timeout2(self):
        n = 100000
        liquids = [1e9 - i for i in range(n)]
        choi.solve(liquids)
