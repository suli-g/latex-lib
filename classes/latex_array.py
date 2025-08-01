from collections.abc import Callable
import numbers
from typing import Iterable
from IPython.display import Latex
import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin
from utils.compile import compile_to_latex


class LatexArray(NDArrayOperatorsMixin, Latex):
    """
    Represents an array in LaTeX format.

    Properties:
        values: The values in the array.
        data: The LaTeX representation of the array.
    """

    def __init__(self, values: Iterable[np.object_]) -> None:
        """
        Initializes a new instance of LatexArray.

        Args:
            values: The values of the array.
        """
        self.value = np.array(values)

    @property
    def data(self):
        return compile_to_latex(self.value)

    def update(
        self, method: Callable[[np.ndarray], np.ndarray], *args, **kwargs
    ) -> "LatexArray":
        """
        Updates the value of the array using the given method.

        Args:
            method: A method that updates the value of an array and
            returns the modified array.

        Returns:
            _description_
        """
        result: np.ndarray = method(self.value, *args, **kwargs)

        # Ensure the given method returns a NumPy array.
        if not isinstance(result, np.ndarray):
            raise ValueError("This method does not return a NumPy array.")

        self.value = result
        return self

    _HANDLED_TYPES = (np.ndarray, numbers.Number, list, tuple)

    def __array_ufunc__[T, V](
        self, ufunc, method, *inputs: T, **kwargs: dict[str, V]
    ) -> "LatexArray":
        """
        Handles ufunc operations on instances of LatexArray.

        This is explained in detail in the official documentation:
        <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__array_ufunc__.html>

        Args:
            ufunc: The ufunc to handle.
            method: The method to handle.
            *inputs: The inputs to the ufunc.
            **kwargs: The keyword arguments to the ufunc.

        Returns:
            The output of the given function.
        """
        out: T = kwargs.get("out", ())

        for x in inputs + out:
            # Only support operations with instances of
            # _HANDLED_TYPES. Use ArrayLike instead of type(self)
            # for isinstance to allow subclasses that don't
            # override __array_ufunc__ to handle ArrayLike objects.
            if not isinstance(x, self._HANDLED_TYPES + (self.__class__,)):
                return NotImplemented

        # Defer to the implementation of the ufunc
        # on unwrapped values.
        inputs = tuple(
            x.value if isinstance(x, self.__class__) else x for x in inputs
        )
        if out:
            kwargs["out"] = tuple(
                x.value if isinstance(x, self.__class__) else x for x in out
            )
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == "at":
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)


if __name__ == "__main__":
    print(1)
