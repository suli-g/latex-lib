"""
Implements the :class:`LatexArray` class.

Classes:
    - `LatexArray`: Represents a NumPy array in LaTeX format.
"""

from typing import Sequence, Self, cast
from IPython.display import Latex
import numpy as np
from utils.compile import compile_to_latex


class LatexArray[T](np.ndarray, Latex):
    """
    Represents a NumPy array in LaTeX format.
    Is rendered in a Jupyter notebook as LaTeX.

    Properties:
        input_array: The values in the array.
        data: The LaTeX representation of the array.
    """

    def __new__(cls: type[Latex], input_array: Sequence[T]) -> "LatexArray[T]":
        """
        Creates a new LatexArray object with the given input array.
        """
        obj: "LatexArray[T]" = cast(
            "LatexArray[T]", np.asarray(input_array).view(cls)
        )
        return obj

    @property
    def data(self: Self) -> str:
        """
        The LaTeX representation of the array.

        Returns:
            The LaTeX representation of the array.
        """
        return compile_to_latex(self)

    @data.setter
    def data(self, _):
        """
        Does nothing.

        Implemented so that the data getter could work correctly.
        """
        # Do nothing.
