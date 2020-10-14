isort $(find pyecharts_snapshot -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 pyecharts_snapshot
black -l 79 tests
