Binomial Coefficients in NumPy/SciPy
####################################

:date: 2012-10-21
:lang: en
:author: Alejandro Weinstein
:category: python

For some reason finding how to compute the `binomial coefficients
<http://en.wikipedia.org/wiki/Binomial_coefficient>`_ using Numpy/SciPy
is harder than it should (I couldn't find the answer in the first page of a
google search).

The answer, though, is quite easy: just use ``scipy.special.binom``. For
example:

.. code-block:: python

   >> import scipy
   >> print scipy.special.binom(10,5)
   252.0
