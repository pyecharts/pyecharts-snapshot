Change log
================================================================================

0.2.0 - 17.04.2019
--------------------------------------------------------------------------------

**Added**

#. use pyppeteer, pythonic puppeteer for rendering pyecharts image

**Removed**

#. python 2, 3.5- support
#. no more phantomjs dependency
#. programmatic rendering capability is removed. NO longer it is integrated with
   pyecharts

0.1.10 - 16.12.2018
--------------------------------------------------------------------------------

**Added**

#. `#33 <https://github.com/pyecharts/pyecharts-snapshot/issues/33>`_: Support
   base64 encoding

0.1.9 - 13.11.2018
--------------------------------------------------------------------------------

**Added**

#. Support eps

**Updated**

#. Loosen the requirement on lml

0.1.8 - 12.09.2018
--------------------------------------------------------------------------------

**Fixed**

#. `#28 <https://github.com/pyecharts/pyecharts-snapshot/issues/28>`_:
   pixel_ratio as a parameter

0.1.7 - 31.05.2018
--------------------------------------------------------------------------------

**Fixed**

#. `#23 <https://github.com/pyecharts/pyecharts-snapshot/issues/23>`_: phantomjs
   on windows does not like absolute path but file uri formatted ones

0.1.6 - 16.05.2018
--------------------------------------------------------------------------------

**Updated**

#. use system temp file instead of current working folder for tmp files

0.1.5 - 11.04.2018
--------------------------------------------------------------------------------

**Updated**

#. better error verbose when phantomjs fails to generate output

0.1.4 - 26.03.2018
--------------------------------------------------------------------------------

**Added**

#. Tighter integration with pyecharts 0.4.2. SnapshotEnvironment extends the
   rendering capability of pyecharts
#. `#16 <https://github.com/pyecharts/pyecharts-snapshot/issues/16>`_: phantomjs
   check fails on windows
#. `#14 <https://github.com/pyecharts/pyecharts-snapshot/issues/14>`_: if the
   output file name has a path, this library fails over

0.1.3 - 12.03.2018
--------------------------------------------------------------------------------

**Added**

#. svg support for pyecharts 0.4.0

0.1.2 - 21.12.2017
--------------------------------------------------------------------------------

**Updated**

#. `#9 <https://github.com/pyecharts/pyecharts-snapshot/issues/9>`_: delay 1.5
   seconds

0.1.1 - 17.12.2017
--------------------------------------------------------------------------------

**Updated**

#. higher resolution screenshots for all platforms: windows and linux.

0.1.0 - 15.12.2017
--------------------------------------------------------------------------------

**Updated**

#. support Mac OS Retina display, high resolution screenshots

0.0.11 - 2.11.2017
--------------------------------------------------------------------------------

**Updated**

#. `#7 <https://github.com/pyecharts/pyecharts-snapshot/pull/7>`_: helpful error
   message on missing phantomjs.

0.0.10 - 23.10.2017
--------------------------------------------------------------------------------

**Updated**

#. pyexcel `pyexcel#105 <https://github.com/pyecharts/pyexcel/issues/105>`_,
   remove gease from setup_requires, introduced by 0.0.9.

0.0.9 - 21.10.2017
--------------------------------------------------------------------------------

**Updated**

#. `#6 <https://github.com/pyecharts/pyecharts-snapshot/pull/6>`_: show better

0.0.8 - 08.09.2017
--------------------------------------------------------------------------------

**Updated**

#. `#5 <https://github.com/pyecharts/pyecharts-snapshot/pull/5>`_: fix

0.0.7 - 26.08.2017
--------------------------------------------------------------------------------

**Updated**

#. Save the output of pyecharts to gif file

0.0.6 - 25.08.2017
--------------------------------------------------------------------------------

**Updated**

#. Allow user to specify a custom delay period in seconds. Default is 0.5s

0.0.5 - 22.08.2017
--------------------------------------------------------------------------------

0.0.4 - 19.08.2017
--------------------------------------------------------------------------------

**Updated**

#.  `#1 <https://github.com/pyecharts/pyecharts-snapshot/pull/1>`_: Support

0.0.3 - 19.08.2017
--------------------------------------------------------------------------------

**Updated**

#. Remove download image arrow on the output file

0.0.2 - 18.08.2017
--------------------------------------------------------------------------------

**Added**

#. Save the output of pyecharts to pdf file

0.0.1 - 17.08.2017
--------------------------------------------------------------------------------

**Added**

#. Save the output of pyecharts to png file
