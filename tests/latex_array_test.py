import unittest

import numpy as np

from classes.latex_array import LatexArray


class TestLatexArray(unittest.TestCase):
    def setUp(self) -> None:
        self.array = LatexArray([1, 2, 3])

    def test_implements_repr_latex(self):
        """
        Tests that the LatexArray class can represent itself as LaTeX.
        """
        self.assertTrue(hasattr(self.array, "_repr_latex_"))

    def test_implements_math_operations(self):
        """
        Tests that the LatexArray class allows math operations.
        """
        doubled = LatexArray([2, 4, 6])
        self.assertTrue(np.all(doubled == self.array + self.array))
        self.assertTrue(np.all(doubled == self.array * 2))

    def test_allows_numpy_instance_methods(self):
        """
        Tests that the LatexArray class allows numpy instance methods.
        """
        self.assertEqual(self.array.sum(), 6)

    def test_allows_numpy_class_methods(self):
        """
        Tests that the LatexArray class allows numpy class methods.
        """
        self.assertEqual(np.sum(self.array), 6)

    def test_math_operations_return_latex_array(self):
        """
        Tests that math operations return a LatexArray object.
        """
        self.assertIsInstance(self.array + self.array, LatexArray)

    def test_numpy_instance_methods_return_latex_array(self):
        """
        Tests that numpy instance methods return a LatexArray object.
        """
        self.assertIsInstance(self.array.sum(), LatexArray)

    def test_numpy_class_methods_return_latex_array(self):
        """
        Tests that numpy instance methods return a LatexArray object.
        """
        self.assertIsInstance(np.sum(self.array), LatexArray)
