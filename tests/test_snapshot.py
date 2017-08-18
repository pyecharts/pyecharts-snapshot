import os
import sys
import filecmp
from io import BytesIO
from nose.tools import raises

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
    assert(filecmp.cmp('output.png', get_fixture('sample.png')))


@patch('subprocess.Popen')
def test_pdf_at_command_line(fake_popen):
    fake_popen.return_value.stdout = BytesIO(get_base64_image())
    args = [
        'snapshot', os.path.join("tests", "fixtures", "render.html"), 'pdf']
    with patch.object(sys, 'argv', args):
        main()
    assert(filecmp.cmp('output.pdf', get_fixture('sample.pdf')))


@raises(Exception)
@patch('subprocess.Popen')
def test_unknown_file_type_at_command_line(fake_popen):
    fake_popen.return_value.stdout = BytesIO(get_base64_image())
    args = [
        'snapshot', os.path.join("tests", "fixtures", "render.html"),
        'moonwalk']
    with patch.object(sys, 'argv', args):
        main()


@patch('subprocess.Popen')
def test_make_a_snapshot(fake_popen):
    fake_popen.return_value.stdout = BytesIO(get_base64_image())
    test_output = 'custom.png'
    make_a_snapshot(os.path.join("tests", "fixtures", "render.html"),
                    test_output)
    assert(filecmp.cmp(test_output, get_fixture('sample.png')))


def test_make_a_snapshot_real():
    # cannot produce a consistent binary matching file
    test_output = 'real.png'
    make_a_snapshot(os.path.join("tests", "fixtures", "render.html"),
                    test_output)
    assert(os.path.exists(test_output))  # exists just fine


def test_make_a_snapshot_real_pdf():
    # cannot produce a consistent binary matching file
    test_output = 'real.pdf'
    make_a_snapshot(os.path.join("tests", "fixtures", "render.html"),
                    test_output)
    assert(os.path.exists(test_output))  # exists just fine


def get_base64_image():
    with open(get_fixture('base64.txt'), 'r') as f:
        content = f.read().replace('\r\n', '')
        return ("," + content).encode('utf-8')


def get_fixture(name):
    return os.path.join("tests", "fixtures", name)
