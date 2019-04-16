pip freeze
nosetests --with-cov --cover-package pyecharts_snapshot --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source pyecharts_snapshot && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
