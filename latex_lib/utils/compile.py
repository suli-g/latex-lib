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

    match values.shape:
        case (_,):
            return PARENTHESIS_TEMPLATE.format(
                values=HORIZONTAL_LIST_TEMPLATE.join(values.astype(str))
            )
        case (_, 1):
            return PARENTHESIS_TEMPLATE.format(
                values=VERTICAL_LIST_TEMPLATE.join(
                    values.flatten().astype(str)
                )
            )
        case (_, _):
            return BRACKETED_TEMPLATE.format(
                values=VERTICAL_LIST_TEMPLATE.join(
                    HORIZONTAL_LIST_TEMPLATE.join(value.flatten().astype(str))
                    for value in values
                )
            )

        case (1, _, _):
            return BRACKETED_TEMPLATE.format(
                values=HORIZONTAL_LIST_TEMPLATE.join(
                    _compile_to_latex_str(value) for value in values
                )
            )
        case (x, _, _):
            return BRACKETED_TEMPLATE.format(
                values=VERTICAL_LIST_TEMPLATE.join(
                    _compile_to_latex_str(value) for value in values
                )
            )
        case x if isinstance(x, tuple):
            return BRACKETED_TEMPLATE.format(
                values=VERTICAL_LIST_TEMPLATE.join(
                    _compile_to_latex_str(value) for value in values
                )
            )
        case _:
            raise ValueError(f"Unsupported shape: {values.shape}")


if __name__ == "__main__":
    test = np.array([[[[[1], [2]], [[1], [2]]]], [[[[1], [2]], [[1], [2]]]]])
    print(test.shape)
    print(compile_to_latex(test))
