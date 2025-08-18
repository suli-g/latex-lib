# LaTeX Lib

This package contains a class for simplifying representation of NumPy arrays using LaTeX syntax in a Jupyter notebook.

## Installation

```bash
pip install -i https://test.pypi.org/simple/ latex-lib
```

## Usage

The `LatexArray` class can be used to handle NumPy arrays that need to displayed.

* This class subclasses the `Latex` class from IPython, which is what IPython uses when displaying the object in a Jupyter notebook as LaTeX.


```python
import numpy as np
from latex_lib import LatexArray as Array

# Declare an array of 12 integers as a row vector.
array: Array = Array(range(12))
array
```





$$
\begin{pmatrix}
0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11
\end{pmatrix}
$$




### Arithemtic Operations

The class supports all arithmetic operations supported by `np.ndarray` (its superclass),
which covers generally all operations.


```python
# Perform some arithmetic on the original array.
(array + array) + 1 * 2 / 5
```





$$
\begin{pmatrix}
0.4 & 2.4 & 4.4 & 6.4 & 8.4 & 10.4 & 12.4 & 14.4 & 16.4 & 18.4 & 20.4 & 22.4
\end{pmatrix}
$$




## NumPy Methods

The class supports all methods supported by `np.ndarray` as well.


```python
# Reshape the array into a column vector.
array.reshape((-1, 1))
```





$$
\begin{pmatrix}
1\\
2\\
3\\
4\\
5\\
6\\
7\\
8\\
9\\
10\\
11
\end{pmatrix}
$$





```python
# Reshape the array into a 6 x 2 matrix.
array.reshape(-1, 2)
```





$$
\begin{bmatrix}
0 & 1\\
2 & 3\\
4 & 5\\
6 & 7\\
8 & 9\\
10 & 11
\end{bmatrix}
$$




## NumPy Class Methods

Numpy functions and class methods are also generally supported (although, edge cases may exist).


```python
# NumPy functions work but do not return a LatexArray object.
np.where(array % 2 == 0, "Even", "Odd")
```




    array(['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd',
           'Even', 'Odd', 'Even'], dtype='<U4')




```python
# We may, however, cast them to one:
Array(np.where(array % 2 == 0, "Even", "Odd"))
```





$$
\begin{pmatrix}
Odd & Even & Odd & Even & Odd & Even & Odd & Even & Odd & Even & Odd & Even
\end{pmatrix}
$$




## Contributing

If you have any questions or suggestions, please feel free to [open an issue](https://github.com/suli-g/latex-lib/issues) or [submit a pull request](https://github.com/suli-g/latex-lib/pulls).

## License

This package is released under the [MIT License](https://github.com/suli-g/latex-lib/blob/main/LICENSE).
