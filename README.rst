================================================================================
pyecharts-snapshot
================================================================================

.. image:: https://api.travis-ci.org/pyecharts/pyecharts-snapshot.svg?branch=master
   :target: http://travis-ci.org/pyecharts/pyecharts-snapshot

.. image:: https://codecov.io/gh/pyecharts/pyecharts-snapshot/branch/master/graph/badge.svg
    :target: https://codecov.io/github/pyecharts/pyecharts-snapshot

Introduction
================================================================================

pyecharts-snapshot renders the output of pyecharts as a png, jpeg, gif, svg image or
a pdf file at command line or in your code.


Please be aware of its dependency on **phantom.js**.

Usage
================================================================================

Get png:

.. code-block:: bash

   $ snapshot render.html

And you will get:

.. image:: https://raw.githubusercontent.com/pyecharts/pyecharts-snapshot/master/images/demo.png
   :width: 800px

Get pdf:

.. code-block:: bash

   $ snapshot render.html pdf

And you will get:

.. image:: https://raw.githubusercontent.com/pyecharts/pyecharts-snapshot/master/images/demo_in_pdf.png
   :target: https://raw.githubusercontent.com/pyecharts/pyecharts-snapshot/master/examples/grid.pdf
   :width: 800px

And here the code to `generate it <https://github.com/pyecharts/pyecharts-snapshot/blob/master/examples/grid.py>`_


Get svg:

.. code-block:: bash

   $ snapshot render.html svg

Please be aware that `render.html` should have configure echarts to do svg rendering. This library, being
stupid, does not make canvas rendered image as svg rendered. Here is `an example svg file <https://github.com/pyecharts/pyecharts-snapshot/master/exampless/cang-zhou.svg>`_.


Usage details
--------------------------------------------------------------------------------

Command line options::

   $ snapshot output.html [png|jpeg|gif|svg|pdf] delay_in_seconds

where `delay_in_seconds` tells pyexcel-snapshot to take a snapshot after
delay_in_seconds. It is needed only when your snapshot is partial because the chart
animation takes long than 0.5 second(default).


Programmatical usage is simple:

.. code-block:: python

   ...
   somechart.render(path='cool_snapshot.png')  # delay=1) for 1 second delay

where delay as an optional parameter can be given to specify `delay_in_seconds`.

Example programs
--------------------------------------------------------------------------------

Here's a fully working example code to get a png image:

.. code-block:: python

   # coding=utf-8
   from __future__ import unicode_literals
   from pyecharts import Bar

   attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
   v1 = [5, 20, 36, 10, 75, 90]
   v2 = [10, 25, 8, 60, 20, 80]
   bar = Bar("柱状图数据堆叠示例")
   bar.add("商家A", attr, v1, is_stack=True)
   bar.add("商家B", attr, v2, is_stack=True)
   bar.render(path='snapshot.png')


Here is the snapshot:

.. image:: https://raw.githubusercontent.com/pyecharts/pyecharts-snapshot/master/images/snapshot.png
   :width: 800px

In order to get a pdf file, you can do the following instead:

.. code-block:: python

   # coding=utf-8
   from __future__ import unicode_literals

   from pyecharts import Line, Pie, Grid, configure

   configure(output_image=True)

   line = Line("折线图示例", width=1200)
   attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
   line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
            mark_point=["max", "min"], mark_line=["average"])
   line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
            mark_line=["average"], legend_pos="20%")
   attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
   v1 = [11, 12, 13, 10, 10, 10]
   pie = Pie("饼图示例", title_pos="45%")
   pie.add("", attr, v1, radius=[30, 55],
           legend_pos="65%", legend_orient='vertical')

   grid = Grid()
   grid.add(line, grid_right="65%")
   grid.add(pie, grid_left="60%")
   grid.render(path='snapshot.pdf')


Here is the snapshot in pdf:

.. image:: https://raw.githubusercontent.com/pyecharts/pyecharts-snapshot/master/images/snapshot_in_pdf.png
   :target: https://raw.githubusercontent.com/pyecharts/pyecharts-snapshot/master/examples/snapshot_in_pdf.pdf
   :width: 800px


Coffee
================================================================================

Please buy `me a coffee <http://pyecharts.org/#/zh-cn/donate>`_ if you think this library helped.


Installation
================================================================================

Tools dependencies
--------------------------------------------------------------------------------

Please install `a node.js binary <https://nodejs.org/en/download/>`_ to your
operating system. Simply download the tar ball, extract it and place its bin
folder in your PATH.

Next, you will need to issue a magic command:

.. code-block:: bash

   $ npm install -g phantomjs-prebuilt

At the end, please verify if it is there:

.. code-block:: bash

   $ which phantomjs

On windows, please try:

.. code-block::

   C: > phantomjs

If you see it there, continue. Otherwise, start from the beginning, ask for help
or thank you for your attention.

Package installation
--------------------------------------------------------------------------------

You can install it via pip:

.. code-block:: bash

    $ pip install pyecharts-snapshot


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/pyecharts/pyecharts-snapshot.git
    $ cd pyecharts-snapshot
    $ python setup.py install

Test status
================================================================================

Fully tested on pypy, python  2.7, 3.3, 3.4, 3.5 and 3.6.

Constraints
================================================================================

Only one image at a time. No 3D image support

Design Considerations
================================================================================

#. Ghost.Py: very hard to install on my own. Dropped
#. Puppeteer: too big to download. Dropped


Maintenance Instructions
================================================================================

#. install pyecharts-snapshot
#. make demo
#. take screenshots of grid.pdf and snapshot.pdf in examples folder
