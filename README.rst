================================================================================
pyecharts-snapshot
================================================================================

.. image:: https://api.travis-ci.org/chfw/pyecharts-snapshot.svg?branch=master
   :target: http://travis-ci.org/chfw/pyecharts-snapshot

.. image:: https://codecov.io/github/chfw/pyecharts-snapshot/coverage.png
    :target: https://codecov.io/github/chfw/pyecharts-snapshot

.. image:: https://readthedocs.org/projects/pyecharts-snapshot/badge/?version=latest
   :target: http://pyecharts-snapshot.readthedocs.org/en/latest/

Introduction
================================================================================

pyecharts-snapshot renders the output of pyecharts as a png image. It is just a
command away:

.. code-block:: bash

   $ snapshot render.html

And you will get::

.. image:: https://raw.githubusercontent.com/chfw/pyecharts-snapshot/raw/master/images/demo.png


Constraints
================================================================================

Only one image at a time. No 3D image support

Installation
================================================================================

Please install [a node.js binary](https://nodejs.org/en/download/) to your
operating system. Simply download the tar ball, extract it and place its bin
folder in your PATH.

Next, you will need to issue a magic command:

.. code-block:: bash

   $ npm install -g phantomjs

At the end, please verify if it is there:

.. code-block:: bash

   $ which phantomjs

If you see it there, continue. Otherwise, start from the begining, ask for help
or thank you for your attention.

You can install it via pip:

.. code-block:: bash

    $ pip install pyecharts-snapshot


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/chfw/pyecharts-snapshot.git
    $ cd pyecharts-snapshot
    $ python setup.py install
