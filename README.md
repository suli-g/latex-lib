# LaTeX Lib

This package contains a class for simplifying representation of NumPy arrays using LaTeX syntax in a Jupyter notebook.

## Installation

```bash
pip install latex-lib
```

## Usage

The `LatexArray` class can be used to handle NumPy arrays that need to displayed.

* This class implements the `_repr_latex_` method, which is what IPython uses when displaying the object in a Jupyter notebook as LaTeX.

```python
from latex_lib import LatexArray

array = LatexArray([1, 2, 3])
python(array)
```

```python
LatexArray([1, 2, 3])
```

```python
array = LatexArray([1, 2, 3])
array.update(lambda x: x + 1)
array
```

## Contributing

If you have any questions or suggestions, please feel free to [open an issue](https://github.com/suli-g/latex-lib/issues) or [submit a pull request](https://github.com/suli-g/latex-lib/pulls).

## License

This project is released under the [MIT License](https://github.com/suli-g/latex-lib/blob/main/LICENSE).