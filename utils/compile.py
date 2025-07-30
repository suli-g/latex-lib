import numpy as np
import numpy.typing as npt

if __name__ != "__main__":
    from .constants import (
        BRACKETED_TEMPLATE,
        PARENTHESIS_TEMPLATE,
        HORIZONTAL_LIST_TEMPLATE,
        VERTICAL_LIST_TEMPLATE,
        INLINE_TEMPLATE,
        MULTILINE_TEMPLATE,
    )
else:
    from constants import (
        BRACKETED_TEMPLATE,
        PARENTHESIS_TEMPLATE,
        HORIZONTAL_LIST_TEMPLATE,
        VERTICAL_LIST_TEMPLATE,
        INLINE_TEMPLATE,
        MULTILINE_TEMPLATE,
    )

type NumberArray = npt.NDArray[np.number]
type LatexArray = str


def compile_to_latex(array: npt.NDArray[np.number]) -> str:
    if array.ndim == 0:
        return INLINE_TEMPLATE.format(value=array.astype(str)[0])
    return MULTILINE_TEMPLATE.format(value=_compile_to_latex_str(array))


def _compile_to_latex_str(values: NumberArray) -> str:
    r"""
    Compiles the given NumPy array into a LaTeX string.

    Args:
        array: The iterable to compile.

    Returns:
        a string representation of the iterable
    """

    match values.ndim:
        case 0:
            raise ValueError("Cannot compile a scalar to LaTeX.")
        case 1:
            return PARENTHESIS_TEMPLATE.format(
                values=HORIZONTAL_LIST_TEMPLATE.join(values.astype(str))
            )
        case 2 if values.shape[-1] == 1:
            return PARENTHESIS_TEMPLATE.format(
                values=VERTICAL_LIST_TEMPLATE.join(
                    values.astype(str).reshape(-1)
                )
            )
        case 2:
            return BRACKETED_TEMPLATE.format(
                values=VERTICAL_LIST_TEMPLATE.join(
                    HORIZONTAL_LIST_TEMPLATE.join(map(str, value))
                    for value in values
                )
            )
        case 3 if values.shape[-1] == 1:
            return BRACKETED_TEMPLATE.format(
                values=HORIZONTAL_LIST_TEMPLATE.join(
                    [
                        _compile_to_latex_str(
                            value.reshape(-1, value.shape[-1])
                        )
                        for value in values
                    ]
                )
            )

        case 3:
            return BRACKETED_TEMPLATE.format(
                values=VERTICAL_LIST_TEMPLATE.join(
                    HORIZONTAL_LIST_TEMPLATE.join(
                        [
                            _compile_to_latex_str(
                                value
                            )
                            for value in sub_array
                        ]
                    )
                    for sub_array in values
                )
            )


if __name__ == "__main__":
    test = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print(test.shape)
    print(compile_to_latex(test.reshape(3, 2, 2)))
