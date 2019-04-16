all: test

test:
	bash test.sh

demo:
	bash images.sh

format:
	isort -y $(find pyecharts_snapshot -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 .
