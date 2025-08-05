import unittest
import numpy as np
from latex_lib.utils.compile import compile_to_latex


class TestCompileVectorsToLatex(unittest.TestCase):
    """
    Test class for compiling vectors to LaTeX,
    """

    ROW_VECTOR = r"""
$$
\begin{pmatrix}
1 & 2 & 3
\end{pmatrix}
$$
"""

    COL_VECTOR = r"""
$$
\begin{pmatrix}
1\\
3
\end{pmatrix}
$$
"""

    def test_compile_row_vector(self):
        """
        Test to make sure that row-vectors compile correctly.
        """
        test = np.array([1, 2, 3])
        self.assertEqual(compile_to_latex(test), self.ROW_VECTOR)

    def test_compile_column_vector(self):
        """
        Test to make sure that column-vectors compile correctly.
        """
        test = np.array([[1], [3]])
        self.assertEqual(compile_to_latex(test), self.COL_VECTOR)
