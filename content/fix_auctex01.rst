Fix error when opening a tex file using emacs 24
################################################

:date: 2012-09-10
:lang: en
:author: Alejandro Weinstein
:category: fix
 
After switching to emacs 24, each time I open a tex file, I was getting the
error:

.. code-block:: console

  Error: Don't know how to compile nil

It turns out this is a well know bug_. To fix_ it, you just need to change two
lines in ``font-latex.el``:

.. code-block:: diff

    -      (byte-compile (intern (concat "font-latex-" name)))
    -      (byte-compile (intern (concat "font-latex-" name "-make"))))))
    +      (byte-compile (intern (concat "font-latex-match-" name)))
    +      (byte-compile (intern (concat "font-latex-match-" name "-make"))))))

After editing the file, you need to byte compile ``font-latex.el``.


.. _bug: http://lists.gnu.org/archive/html/bug-gnu-emacs/2012-07/msg00023.html
.. _fix: http://cvs.savannah.gnu.org/viewvc/auctex/auctex/font-latex.el?r1=5.193&r2=5.194
