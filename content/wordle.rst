A tag cloud of my thesis
########################

:date: 2013-05-26
:lang: en
:author: Alejandro Weinstein
:category: util

I wanted to create a `tag cloud <http://en.wikipedia.org/wiki/Wordle>`_ of my
thesis, which is written in LaTeX. This is almost trivial. You can go to
`Wordle <http://www.wordle.net/>`_, upload the text, click "Go", and you're
ready to go. Except that being written in LaTeX, if you just do that you will
see a lot of irrelevant markup (begin, end, includegraphics, etc) words in the
word cloud.

An easy way to solve this is to use a program called ``detex``, that transform
a LaTeX source document into plain text. All you just need to do is the
following:


.. code-block:: bash

   $ detex -l *.tex > thesis.txt

Since I have the document divided in several files, I need to use the ``-l``
option to force ``detex`` to use LaTeX mode (without a ``\begin{document}``
``detex`` doesn't use this mode automatically). Then you can upload
``thesis.txt`` to Wordle and you are good to go.

This is the result:

.. image:: static/images/wordle.png
   :width: 700 px


