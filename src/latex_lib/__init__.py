"""
Implements packages to simplify representation
of NumPy arrays using LaTeX syntax.

Packages:
    - `latex_array` implements classes for representing
      arrays in LaTeX format.
    - `utils` provides utility functions for working
      with arrays.
"""

from .classes.latex_array import LatexArray
from .utils.compile import compile_to_latex

__all__ = ["LatexArray", "compile_to_latex"]
