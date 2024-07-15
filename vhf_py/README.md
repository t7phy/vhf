#### Rust crate for low level computation

To install the python bindings, first one needs to install `maturin`:
```bash
pip install maturin
```
then compile the codes using the following command:
```bash
maturin develop
```
To test that the python module has been generated properly, invoke a python interpreter and check:
```python
Python 3.10.14 (main, May  6 2024, 19:42:50) [GCC 11.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from vhf_py import hr2

In [2]: hr2(0, 0, 2.5)
Out[2]: 0.4197943526592374
```
