[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dewloosh/nddict/main?labpath=examples%2Fbasic_examples.ipynb?urlpath=lab)
[![CircleCI](https://circleci.com/gh/dewloosh/nddict.svg?style=shield)](https://circleci.com/gh/dewloosh/nddict) 
[![Documentation Status](https://readthedocs.org/projects/nddict/badge/?version=latest)](https://nddict.readthedocs.io/en/latest/?badge=latest) 
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# **nddict** - A nested dictionary class with a self-replicating default factory

 
Minimal example:

```python
>>> from nddict import DeepDict
>>> d = {'a' : {'aa' : {'aaa' : 0}}, 'b' : 1, 'c' : {'cc' : 2}}
>>> dd = DeepDict(d)
>>> list(dd.values(deep=True))
[0, 1, 2]
```

## **Documentation and Issues**

Click [here](https://nddict.readthedocs.io/en/latest/) to read the documentation.

There are no known issues.

## **Testing**

To run all tests, open up a console in the root directory of the project and type the following

```console
>>> python -m unittest
```

## **License**

This package is licensed under the MIT license.
