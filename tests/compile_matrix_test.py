import unittest
import numpy as np
from utils.compile import compile_to_latex


class TestCompileMatrixToLatex(unittest.TestCase):
    MATRIX_3_BY_4 = r"""
$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8 \\
9 & 10 & 11 & 12
\end{bmatrix}
$$
"""

    MATRIX_3_BY_2_BY_2 = r"""
$$
\begin{bmatrix}
\begin{pmatrix}
1 & 2
\end{pmatrix} & \begin{pmatrix}
3 & 4
\end{pmatrix} \\
\begin{pmatrix}
5 & 6
\end{pmatrix} & \begin{pmatrix}
7 & 8
\end{pmatrix} \\
\begin{pmatrix}
9 & 10
\end{pmatrix} & \begin{pmatrix}
11 & 12
\end{pmatrix}
\end{bmatrix}
$$
"""
    VALUES = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_compile_3_by_4_matrix(self):
        """
        Test to make sure that 3-by-4 matrices compile correctly.
        """
        self.assertEqual(
            compile_to_latex(self.VALUES.reshape(3, 4)), self.MATRIX_3_BY_4
        )

    def test_compile_3_by_2_by_2_matrix(self):
        """
        Test to make sure that 3-by-3 matrices compile correctly.
        """
        test = self.VALUES.reshape((3, 2, 2))
        self.assertEqual(compile_to_latex(test), self.MATRIX_3_BY_2_BY_2)
