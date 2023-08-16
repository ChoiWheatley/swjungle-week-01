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
