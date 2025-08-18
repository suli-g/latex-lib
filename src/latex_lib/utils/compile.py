import numpy as np
import numpy.typing as npt
from .constants import (
    BRACKETED_TEMPLATE,
    PARENTHESIS_TEMPLATE,
    HORIZONTAL_LIST_TEMPLATE,
    VERTICAL_LIST_TEMPLATE,
    INLINE_TEMPLATE,
    MULTILINE_TEMPLATE,
)


def compile_to_latex(array: npt.NDArray) -> str:
    if array.ndim == 0:
        return INLINE_TEMPLATE.format(value=array.astype(str))
    return MULTILINE_TEMPLATE.format(value=_compile_to_latex_str(array))


def _compile_to_latex_str(values: npt.NDArray) -> str:
    r"""
    Compiles the given NumPy array into a LaTeX string.

    Args:
        array: The iterable to compile.

    Returns:
        a string representation of the iterable
    """
    # List 1-dimension items horizontally.
    if values.ndim <= 1:
        return PARENTHESIS_TEMPLATE.format(
            values=HORIZONTAL_LIST_TEMPLATE.join(values.astype(str))
        )
    elif values.ndim <= 2 and values.shape[1] == 1:
        # List 2-dimension items vertically if paired in subarrays.
        return PARENTHESIS_TEMPLATE.format(
            values=VERTICAL_LIST_TEMPLATE.join(values.flatten().astype(str))
        )
    elif values.ndim <= 2 and values.shape[0] == 1:
        # List 2-dimension items horizontally if unpaired in subarrays.
        return PARENTHESIS_TEMPLATE.format(
            values=HORIZONTAL_LIST_TEMPLATE.join(values.flatten().astype(str))
        )
    elif values.ndim <= 2:
        # Create a grid of both vertical and horizontal elements if
        # there are mixed groups.
        return BRACKETED_TEMPLATE.format(
            values=VERTICAL_LIST_TEMPLATE.join(
                HORIZONTAL_LIST_TEMPLATE.join(v.flatten())
                for v in values.astype(str)
            )
        )
    elif values.ndim % 2 == 0:
        # Stack pairs vertically.
        return BRACKETED_TEMPLATE.format(
            values=VERTICAL_LIST_TEMPLATE.join(
                _compile_to_latex_str(value) for value in values
            )
        )
    else:
        # Stack single subarrays horizontally.
        return BRACKETED_TEMPLATE.format(
            values=HORIZONTAL_LIST_TEMPLATE.join(
                _compile_to_latex_str(value) for value in values
            )
        )
