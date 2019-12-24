# Trutht


Main code by [chicolucio ( Francisco Bustamante )] from *[truth-table-generator]* (https://github.com/chicolucio/truth-table-generator) and by [tr3buchet] from *[truths]* (https://github.com/tr3buchet/truths) with my modifications.

Main README.md file by [chicolucio ( Francisco Bustamante )] from *[truth-table-generator]* (https://github.com/chicolucio/truth-table-generator) with my modifications.


**Python API for truth tables**

It merges some of the pull requests in the original and other external helpers.
The following are some of the changes and enhancements from the original:

- [tabulate](https://github.com/astanin/python-tabulate) instead of obsolete
[prettytable](https://code.google.com/archive/p/prettytable/) as main tool to
represent tabular data in ASCII tables (PrettyTable version is still available).
    - so there are many table formats available as such LaTeX, Org Tables, HTML
    and all others cited on [tabulate docs](https://github.com/astanin/python-tabulate)
- the table is now a Pandas DataFrame so you can make the output more visually
appealing with [Pandas Styling](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html).
See examples below.
- new function `valuation` that eval a proposition as a tautology, contradiction
or contingency.
- new command line interface (CLI) for printing a truth table from terminal.

## Installation

`pip install trutht`


## Usage

### Importing and syntax

First, let's import the package. `trutht` stands for *truth-table-generator*.

```python
import trutht
```

A truth table has one column for each input variable (for example, *x* and *y*),
and one final column showing all of the possible results of the logical
operation that the table represents. If the input has only one list of strings,
each string is considered an input variable:

```python
print(trutht.Truths(['x', 'y', 'z']))
```
```
+-----+-----+-----+
|  x  |  y  |  z  |
|-----+-----+-----|
|  0  |  0  |  0  |
|  0  |  0  |  1  |
|  0  |  1  |  0  |
|  0  |  1  |  1  |
|  1  |  0  |  0  |
|  1  |  0  |  1  |
|  1  |  1  |  0  |
|  1  |  1  |  1  |
+-----+-----+-----+
```

A second list of strings can be passed with propositional expressions created
with logical operators.

```python
print(trutht.Truths(['x', 'y', 'z'], ['x and y and z', 'x or y or z', '(x or (not y)) imp z']))
```
```
+-----+-----+-----+-----------------+---------------+------------------------+
|  x  |  y  |  z  |  x and y and z  |  x or y or z  |  (x or (not y)) imp z  |
|-----+-----+-----+-----------------+---------------+------------------------|
|  0  |  0  |  0  |        0        |       0       |            0           |
|  0  |  0  |  1  |        0        |       1       |            1           |
|  0  |  1  |  0  |        0        |       1       |            1           |
|  0  |  1  |  1  |        0        |       1       |            1           |
|  1  |  0  |  0  |        0        |       1       |            0           |
|  1  |  0  |  1  |        0        |       1       |            1           |
|  1  |  1  |  0  |        0        |       1       |            0           |
|  1  |  1  |  1  |        1        |       1       |            1           |
+-----+-----+-----+-----------------+---------------+------------------------+
```

### Operators and their representations:

- *negation*: `'not'`
- *logical disjunction*: `'or'`
- *logical nor*: `'nor'`
- *exclusive disjunction*: `'xor'`
- *logical conjunction*:  `'and'`
- *logical NAND*: `'not_and'`
- *material implication*: `'imp'`
- *reversed material implication*: `'r_imp'`
- *logical biconditional*: `'equ'`
- *Reversed logical biconditional*: `'r_equ'`

**Note**: Use parentheses! Especially with the negation operator. Use tables
above and below as reference. Although precedence rules are used, sometimes
precedence between conjunction and disjunction is unspecified requiring to
 provide it explicitly in given formula with parentheses.

### Showing words (True / False)

If you prefer the words True and False instead of numbers 0 and 1, there is a
third parameter, boolean type, `ints` that can be set to `False`:

```python
print(trutht.Truths(['x', 'y'], ['x and y', 'x or y', '(x or (not y)) imp (not x)'], ints=False))
```
```
+-------+-------+-----------+----------+-----------------------------+
|   x   |   y   |  x and y  |  x or y  |  (x or (not y)) imp (not x)  |
|-------+-------+-----------+----------+-----------------------------|
| False | False |   False   |   False  |            True             |
| False | True  |   False   |   True   |            True             |
| True  | False |   False   |   True   |            False            |
| True  | True  |   True    |   True   |            False            |
+-------+-------+-----------+----------+-----------------------------+
```

### Formatting options with PrettyTable and Tabulate

For more formatting options, let's create a truth table variable:
```python
table = trutht.Truths(['x', 'y'], ['x imp y', 'x equ y'])
```
The command `print(table)` renders the standard table as seen on above examples:
```
+-----+-----+----------+------------+
|  x  |  y  |  x imp y  |  x equ y  |
|-----+-----+----------+------------|
|  0  |  0  |     1     |     1     |
|  0  |  1  |     1     |     0     |
|  1  |  0  |     0     |     0     |
|  1  |  1  |     1     |     1     |
+-----+-----+----------+------------+
```
The command `print(table.as_prettytable())` renders the table with PrettyTable
package as on the original version of this package:
```
+---+---+---------+---------+
| x | y | x imp y | x equ y |
+---+---+---------+---------+
| 0 | 0 |    1    |    1    |
| 0 | 1 |    1    |    0    |
| 1 | 0 |    0    |    0    |
| 1 | 1 |    1    |    1    |
+---+---+---------+---------+
```
As can be seen, the PrettyTable output has less blank spaces. However, the
PrettyTable package has much less output options and it is deprecated. So I
decided to use the Tabulate package as standard.


### Formatting options with Pandas

With an IPython terminal or a Jupyter Notebook, it is possible to render a Pandas
DataFrame with `table.as_pandas()`:

![pandas01](https://raw.githubusercontent.com/chicolucio/truth-table-generator/master/images/pandas01.png)

And this output can be modified with Pandas Styling

![pandas02](https://raw.githubusercontent.com/chicolucio/truth-table-generator/master/images/pandas02.png)

More advanced modifications can be done with functions that apply styling changes.
See the [styles tutorial notebook](styling_tutorial.ipynb) for examples.
See the image below for a fancy example with two lines and two columns
highlighted with yellow background and different colors for True and False.

![pandas03](https://raw.githubusercontent.com/chicolucio/truth-table-generator/master/images/pandas03.png)

### The `valuation` function

Let's see the how to use the `valuation` function with a new truth table:
```python
table_val = trutht.Truths(['x', 'y'], ['x = y', 'x and (not x)', '(x and y) => x'])
print(table_val)
```
```
+-----+-----+-----------+-----------------+------------------+
|  x  |  y  |  x equ y  |  x and (not x)  |  (x and y) imp x |
|-----+-----+-----------+-----------------+------------------|
|  0  |  0  |     1     |        0        |        1         |
|  0  |  1  |     0     |        0        |        1         |
|  1  |  0  |     0     |        0        |        1         |
|  1  |  1  |     1     |        0        |        1         |
+-----+-----+---------+-------------------+------------------+
```
Without arguments, the `valuation` function classifies the *last column* as a
tautology, a contradiction or a contingency:
```python
table_val.valuation()
```
```
'Tautology'
```
If a integer is used as argument, the function classifies the correspondent
column:
```python
table_val.valuation(3)
```
```
'Contingency'
```
```python
table_val.valuation(4)
```
```
'Contradiction'
```

### CLI utility

For those who work in the terminal there is a simple command line interface
(CLI) for printing tables. The script name is `ttg_cly.py` and it accepts
the following syntax according to its `--help`:

```
usage: trutht_cli.py [-h] [-p PROPOSITIONS] [-i INTS] variables

positional arguments:
  variables             List of variables e. g. "['p', 'q']"

optional arguments:
  -h, --help            show this help message and exit
  -p PROPOSITIONS, --propositions PROPOSITIONS
                        List of propositions e. g. "['p or q', 'p and q']"
  -i INTS, --ints INTS  True for 0 and 1; False for words
```

As seen, the list of variables is mandatory. Note that the lists must be between
`"`.

```bash
$ trutht_cli.py "['x', 'y', 'z']"
```
```
+-----+-----+-----+
|  x  |  y  |  z  |
|-----+-----+-----|
|  0  |  0  |  0  |
|  0  |  0  |  1  |
|  0  |  1  |  0  |
|  0  |  1  |  1  |
|  1  |  0  |  0  |
|  1  |  0  |  1  |
|  1  |  1  |  0  |
|  1  |  1  |  1  |
+-----+-----+-----+
```

The real look of the table depends on your terminal appearance configuration.
The green on black background screenshots from the first picture of this README
are from my terminal.

## Contributing

All contributions are welcome.

**Issues**

Feel free to submit issues regarding:

- recommendations
- more examples for the tutorial
- enhancement requests and new useful features
- code bugs

**Pull requests**

- before starting to work on your pull request, please submit an issue first
- fork the repo
- clone the project to your own machine
- commit changes to your own branch
- push your work back up to your fork
- submit a pull request so that your changes can be reviewed


## License

Apache 2.0, see [LICENSE](LICENSE)
