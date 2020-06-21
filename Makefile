all: test

test: lint
	bash test.sh

install_test:
	pip install -r tests/requirements.txt

git-diff-check:
	git diff --exit-code

lint:
	bash lint.sh

format:
	isort -y $(find pyecharts_snapshot -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 pyecharts_snapshot
	black -l 79 tests

git-diff-check:
	git diff --exit-code
