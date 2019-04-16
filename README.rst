================================================================================
pyecharts-snapshot
================================================================================

.. image:: https://api.travis-ci.org/pyecharts/pyecharts-snapshot.svg?branch=master
   :target: http://travis-ci.org/pyecharts/pyecharts-snapshot

.. image:: https://dev.azure.com/pyecharts/pyecharts-snapshot/_apis/build/status/pyecharts.pyecharts-snapshot
   :target: https://dev.azure.com/pyecharts/pyecharts-snapshot/_build?definitionId=1&_a=summary

.. image:: https://codecov.io/gh/pyecharts/pyecharts-snapshot/branch/master/graph/badge.svg
    :target: https://codecov.io/github/pyecharts/pyecharts-snapshot


News - 16.04.2019
================================================================================

Since 0.2.0, NO LONGER, phantomjs is required! NO LONGER, it supports python 2.7

BUT, the capability to render pyecharts in a script has been merged into
pyecharts 1.0.0. And the dependency on phantomjs has been sprawn as:
`snapshot-phantomjs <https://github.com/pyecharts/snapshot-phantomjs>`_ .

If you love to use 'snapshot' command line, please continue to use this
project. 

Introduction
================================================================================

pyecharts-snapshot renders the output of pyecharts/echarts.js as a png, jpeg,
gif, eps, svg image, raw base64 encoding or a pdf file at command line.


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

   $ snapshot output.html [png|jpeg|gif|svg|pdf] [delay] [pixel ratio]

where:

`delay` tells pyecharts-snapshot to take a snapshot after
some time measured in seconds. It is needed only when your snapshot is partial because the chart
animation takes long than 1.5 second(default).
`pixel ratio` tells pyecharts-snapshot to use a different pixel ratio when generate
the image. It defaults to 2.


Programmatical usage is simple:

.. code-block:: python

   ...
   somechart.render(path='cool_snapshot.png')  # delay=1, pixel_ratio=3) 1 second delay, 3 as pixel ratio

where delay as an optional parameter can be given to specify `delay_in_seconds`.

Coffee
================================================================================

Please buy `me a coffee <http://pyecharts.org/#/zh-cn/donate>`_ if you think this library helped.


Installation
================================================================================

Package installation
--------------------------------------------------------------------------------

You can install it via pip:

.. code-block:: bash

    $ pip install pyecharts-snapshot
    $ pyppeteer-install


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/pyecharts/pyecharts-snapshot.git
    $ cd pyecharts-snapshot
    $ python setup.py install
    $ pyppeteer-install

.. note::

   pyppeteer-install is recommended but optional. Your first ever run of
   **snapshot** command will invoke pyppeteer-install. This command will
   download `Chrominium <https://www.chromium.org>`_,
   `about 100MB <https://github.com/miyakogi/pyppeteer#usage>`_

Test status
================================================================================

Fully tested on pypy, python 3.5, 3.6, 3.7 and 3.8-dev.

Constraints
================================================================================

Only one image at a time. No 3D image support

Design Considerations
================================================================================

#. Ghost.Py: very hard to install on my own. Dropped


Maintenance Instructions
================================================================================

#. install pyecharts-snapshot
#. make demo
#. take screenshots of grid.pdf and snapshot.pdf in examples folder
