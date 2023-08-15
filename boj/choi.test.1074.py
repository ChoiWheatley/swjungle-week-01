from ex1074 import sol_recur
import unittest


class Test(unittest.TestCase):
    def test_dim_3(self):
        answer = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
            (0, 2),
            (0, 3),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (3, 0),
            (3, 1),
            (2, 2),
            (2, 3),
            (3, 2),
            (3, 3),
            (0, 4),
            (0, 5),
            (1, 4),
            (1, 5),
        ]
        for idx, (row, col) in enumerate(answer):
            self.assertEqual(
                idx,
                sol_recur(3, row, col, 0, 2 ** (2 * 3)),
                f"☠️ row: {row}, col: {col} ☠️",
            )


if __name__ == "__main__":
    unittest.main()
