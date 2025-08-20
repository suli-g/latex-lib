INLINE_TEMPLATE = """
${value}$
"""
"""A template for inline values in LaTeX."""

MULTILINE_TEMPLATE = """
$$
{value}
$$
"""
"""A template for multiline values in LaTeX."""

ALIGNED_TEMPLATE = r"""\begin{{align*}}
{values}
\end{{align*}}"""
"""A template for aligning multiple values in LaTeX."""

BRACKETED_TEMPLATE = r"""\begin{{bmatrix}}
{values}
\end{{bmatrix}}"""
"""A template for bracketing multiple values in LaTeX."""

PARENTHESIS_TEMPLATE = r"""\begin{{pmatrix}}
{values}
\end{{pmatrix}}"""
"""A template for parenthesising multiple values in LaTeX."""

HORIZONTAL_LIST_TEMPLATE = " & "
"""A string used to separate items in a horizontal list in LaTeX."""

VERTICAL_LIST_TEMPLATE = rf"\\{'\n'}"
"""A string used to separate items in a vertical list in LaTeX."""
