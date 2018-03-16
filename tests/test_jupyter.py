import os
from pyecharts import Bar
from pyecharts_snapshot.jupyter import SnapshotEnvironment

from jinja2 import FileSystemLoader


def create_an_env():
    return SnapshotEnvironment(
        loader=FileSystemLoader(
            os.path.join(os.path.dirname(__file__), 'fixtures'))
    )


def create_a_bar(title, renderer='canvas'):
    CLOTHES = ['a', 'b', 'c', 'd', 'e', 'f']
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar(title, renderer=renderer)
    bar.add("A", CLOTHES, v1, is_stack=True)
    bar.add("B", CLOTHES, v2, is_stack=True)
    return bar


def test_snapshot_env():
    env = create_an_env()
    assert env.render_chart_to_notebook() is None


def test_render_chart_to_file():
    env = create_an_env()
    bar = create_a_bar('test')
    content = env.render_chart_to_file(bar)
    assert os.path.exists('render.png')
    assert content is not None
