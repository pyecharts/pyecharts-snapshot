import os
import sys
import filecmp
from io import BytesIO


from pyecharts_snapshot.main import main, make_a_snapshot
try:
    from mock import patch
except ImportError:
    from unittest.mock import patch


@patch('subprocess.Popen')
def test_main(fake_popen):
    fake_popen.return_value.stdout = BytesIO(get_base64_image())
    args = ['snapshot', os.path.join("tests", "fixtures", "render.html")]
    with patch.object(sys, 'argv', args):
        main()
    assert(os.path.exists('output.png'))
    assert(filecmp.cmp('output.png', get_fixture('sample.png')))


@patch('subprocess.Popen')
def test_make_a_snapshot(fake_popen):
    fake_popen.return_value.stdout = BytesIO(get_base64_image())
    test_output = 'custom.png'
    make_a_snapshot(os.path.join("tests", "fixtures", "render.html"),
                    test_output)
    assert(filecmp.cmp(test_output, get_fixture('sample.png')))


def get_base64_image():
    with open(get_fixture('base64.txt'), 'r') as f:
        content = f.read().replace('\r\n', '')
        return ("," + content).encode('utf-8')


def get_fixture(name):
    return os.path.join("tests", "fixtures", name)
