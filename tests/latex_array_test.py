import unittest

import numpy as np

from classes.latex_array import LatexArray


class TestLatexArray(unittest.TestCase):
    def setUp(self) -> None:
        self.array = LatexArray([1, 2, 3])

    def test_implements_repr_latex(self):
        self.assertTrue(hasattr(self.array, "_repr_latex_"))

    def test_implements_allows_math_operations(self):
        self.assertEqual(self.array + self.array, LatexArray([2, 4, 6]))

    def test_allows_numpy_instance_methods(self):
        self.assertEqual(self.array.sum(), 6)

    def test_allows_numpy_class_methods(self):
        self.assertEqual(np.sum(self.array), 6)
