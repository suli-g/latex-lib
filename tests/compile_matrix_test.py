import unittest
import numpy as np
from utils.compile import compile_to_latex


class TestCompileMatrixToLatex(unittest.TestCase):
    MATRIX_3_BY_3 = r"""
$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$
"""

    def test_compile_3_by_3_matrix(self):
        """
        Test to make sure that 3-by-3 matrices compile correctly.
        """
        test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(compile_to_latex(test), self.MATRIX_3_BY_3)
