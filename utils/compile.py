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


type NumberArray = npt.NDArray[np.number]
type LatexArray = str


def compile_to_latex(values: NumberArray) -> str:
    r"""
    Compiles the given NumPy array into a LaTeX string.

    Args:
        array: The iterable to compile.

    Returns:
        a string representation of the iterable
    """

    match values.ndim:
        case 0:
            return INLINE_TEMPLATE.format(value=str(values))
        case 1:
            return MULTILINE_TEMPLATE.format(
                value=PARENTHESIS_TEMPLATE.format(
                    values=HORIZONTAL_LIST_TEMPLATE.join(values.astype(str))
                )
            )
        case 2 if values.shape[-1] == 1:
            return MULTILINE_TEMPLATE.format(
                value=PARENTHESIS_TEMPLATE.format(
                    values=VERTICAL_LIST_TEMPLATE.join(
                        values.astype(str).reshape(-1)
                    )
                )
            )
        case 2:
            return MULTILINE_TEMPLATE.format(
                value=BRACKETED_TEMPLATE.format(
                    values=VERTICAL_LIST_TEMPLATE.join(
                        HORIZONTAL_LIST_TEMPLATE.join(map(str, value))
                        for value in values
                    )
                )
            )
        case _:
            return MULTILINE_TEMPLATE.format(
                value=compile_to_latex(values.reshape(-1, values.shape[-1]))
            )


if __name__ == "__main__":

    test = np.array([[1, 2, 3]])
    print(compile_to_latex(test))
