================================================================================
pyecharts-snapshot
================================================================================

.. image:: https://api.travis-ci.org/chfw/pyecharts-snapshot.svg?branch=master
   :target: http://travis-ci.org/chfw/pyecharts-snapshot

.. image:: https://codecov.io/gh/chfw/pyecharts-snapshot/branch/master/graph/badge.svg
    :target: https://codecov.io/github/chfw/pyecharts-snapshot

Introduction
================================================================================

pyecharts-snapshot renders the output of pyecharts as a png image. 


Quick usage:

.. code-block:: bash

   $ snapshot render.html

And you will get:

.. image:: https://raw.githubusercontent.com/chfw/pyecharts-snapshot/master/images/demo.png

Please find the corresponding code in `examples <https://github.com/chfw/pyecharts-snapshot/tree/master/examples>`_ folder.


Test status
================================================================================

Fully tested on pypy, python 2.6, 2.7, 3.3, 3.4, 3.5 and 3.6.

Constraints
================================================================================

Only one image at a time. No 3D image support


Installation
================================================================================

Tools dependencies
--------------------------------------------------------------------------------

Please install `a node.js binary <https://nodejs.org/en/download/>`_ to your
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

Package installation
--------------------------------------------------------------------------------

You can install it via pip:

.. code-block:: bash

    $ pip install pyecharts-snapshot


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/chfw/pyecharts-snapshot.git
    $ cd pyecharts-snapshot
    $ python setup.py install


Usages
================================================================================

Programmatical usage is simple:

.. code-block:: python

   from pyecharts_snapshot.main import make_a_snapshot

   ...
   somechart.render()
   make_a_snapshot('render.html', 'cool_snapshot.png')

Here's a fully working example code:

.. code-block:: python

   # coding=utf-8
   from __future__ import unicode_literals
   from pyecharts import Bar
   from pyecharts_snapshot.main import make_a_snapshot
   
   attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
   v1 = [5, 20, 36, 10, 75, 90]
   v2 = [10, 25, 8, 60, 20, 80]
   bar = Bar("柱状图数据堆叠示例")
   bar.add("商家A", attr, v1, is_stack=True)
   bar.add("商家B", attr, v2, is_stack=True)
   bar.render()
   make_a_snapshot('render.html', 'snapshot.png')


Here is the snapshot:

.. image:: https://raw.githubusercontent.com/chfw/pyecharts-snapshot/master/images/snapshot.png

