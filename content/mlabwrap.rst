A patched mlabwrap
##################

:date: 2012-10-19
:lang: en
:author: Alejandro Weinstein
:category: fix
 
mlabwrap_ is a Python library that allows you to run MATLAB code from Python. 

I get the following error when trying to install the last version (v1.1) in my
machine (Lubuntu 12.04, Python 2.7)

.. code-block:: console

  mlabraw.cpp:225: *error*: invalid conversion from ‘const mwSize*’ to ‘const int*’

I fixed this by following this instructions_. 

For everyone's convenience, I created a repository at github with a patched
version of mlabwrap:

https://github.com/aweinstein/mlabwrap

Enjoy!

.. _mlabwrap: http://mlabwrap.sourceforge.net/
.. _instructions: http://sourceforge.net/mailarchive/message.php?msg_id=27312822
