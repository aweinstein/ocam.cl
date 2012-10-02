Using NumPy masked arrays
#########################

:date: 2012-10-02
:lang: en
:author: Alejandro Weinstein
:category: python
 
In NumPy, masked arrays are quite handy. Say you want to find the index of the
smallest positive entry of an array. Doing `a[a>0].argmin()` doesn't work,
because you're removing all the non-positive numbers from `a`, so you're
computing `argmin` over the wrong array.

Masked arrays provide an easy solution to this problem. The following code shows how:

.. code-block:: python

   import numpy as np

   np.random.seed(42) # Just to get always the same output

   a = np.random.randint(-10, 10, (1, 10))
   mask = np.zeros_like(a, dtype='bool')
   a_masked = np.ma.masked_array(a)
   a_masked[a <= 0] = np.ma.masked
   
   print 'a:', a
   print 'a.argmin():', a.argmin()
   print 'a.min():',a.min()
   print
   print 'a_masked:', a_masked
   print 'a_masked.argmin():', a_masked.argmin()
   print 'a_masked.min():',a_masked.min()

And the output is:

.. code-block:: python

   a: [[-4  9  4  0 -3 -4  8  0  0 -7]]
   a.argmin(): 9
   a.min(): -7

   a_masked: [[-- 9 4 -- -- -- 8 -- -- --]]
   a_masked.argmin(): 2
   a_masked.min(): 4
