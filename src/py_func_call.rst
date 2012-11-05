Using a command line parameter to specify the name of a function to call
########################################################################

:date: 2012-11-05
:lang: en
:author: Alejandro Weinstein
:category: python

When running some Python experiments, where typically each experiment
corresponds to run a simulation under some particular conditions, I find useful
to be able to call a particular function from the command line. For example, if
I define the functions ``exp_1``, ``exp_2``, and ``exp_3``, I want to be able
to do the following from the command line:

.. code-block:: bash

    $ python my_script.py exp_1
    Running experiment 1...

The following code allows this:

.. code-block:: python

    def exp_1():
        print 'Running experiment 1...'
        # Do some stuff

    def exp_2():
        print 'Running experiment 2...'
        # Do some stuff

    def exp_3():
        print 'Running experiment 3...'
        # Do some stuff
		
    if __name__ == '__main__':
        import sys
    
        if len(sys.argv) == 2:
            fname = sys.argv[1]
            if locals().has_key(fname) and hasattr(locals()[fname], '__call__'):
                locals()[fname]()
            else:
                print 'Function %s does not exist' % fname
        else:
            print 'Wrong number of arguments'
    
Note that if you're using IPython, you can do

.. code-block:: python

    In [1]: run foo exp_1
    Running experiment 1...
