import os
import sys
import codecs
import filecmp
from io import BytesIO
from mock import patch
from nose.tools import raises, eq_
from platform import python_implementation

from pyecharts_snapshot.main import main, make_a_snapshot, PY2
from pyecharts_snapshot.main import save_as_svg, to_file_uri

PY27 = sys.version_info[1] == 7 and PY2 and python_implementation() != "PyPy"
HTML_FILE = os.path.join("tests", "fixtures", "render.html")
SVG_HTML_FILE = os.path.join("tests", "fixtures", "render_svg_cangzhou.html")


class CustomTestException(Exception):
    pass


class TestMain():

    def setUp(self):
        self.patcher = patch("subprocess.Popen")
        self.fake_popen = self.patcher.start()
        self.patcher1 = patch("subprocess.check_output")
        self.fake_call = self.patcher1.start()

    def tearDown(self):
        self.patcher1.stop()
        self.patcher.stop()

    @raises(SystemExit)
    def test_no_params(self):
        args = ["snapshot"]
        with patch.object(sys, "argv", args):
            main()

    @raises(SystemExit)
    def test_help(self):
        args = ["snapshot", "help"]
        with patch.object(sys, "argv", args):
            main()

    @raises(SystemExit)
    def test_no_phantomjs(self):
        self.fake_call.side_effect = OSError
        args = ["snapshot", "a", "png"]
        with patch.object(sys, "argv", args):
            main()

    def test_main(self):
        self.fake_popen.return_value.stdout = BytesIO(get_base64_image())
        args = ["snapshot", HTML_FILE]
        with patch.object(sys, "argv", args):
            main()
        assert filecmp.cmp("output.png", get_fixture("sample.png"))

    def test_jpeg_at_command_line(self):
        self.fake_popen.return_value.stdout = BytesIO(get_base64_image())
        args = ["snapshot", HTML_FILE, "jpeg"]
        with patch.object(sys, "argv", args):
            main()
        assert filecmp.cmp("output.jpeg", get_fixture("sample.jpeg"))

    def test_pdf_at_command_line(self):
        self.fake_popen.return_value.stdout = BytesIO(get_base64_image())
        args = ["snapshot", HTML_FILE, "pdf"]
        with patch.object(sys, "argv", args):
            main()
        assert os.path.exists("output.pdf")

    def test_delay_option(self):
        self.fake_popen.side_effect = Exception("Enough test. Abort")
        sample_delay = 0.1
        args = ["snapshot", HTML_FILE, "jpeg", str(sample_delay)]
        try:
            with patch.object(sys, "argv", args):
                main()
        except Exception:
            eq_(self.fake_popen.call_args[0][0][4], "100")

    def test_pixcel_option(self):
        self.fake_popen.side_effect = Exception("Enough test. Abort")
        pixel_ratio = 5
        args = ["snapshot", HTML_FILE, "jpeg", "0.1", str(pixel_ratio)]
        try:
            with patch.object(sys, "argv", args):
                main()
        except Exception:
            print(self.fake_popen.call_args)
            eq_(self.fake_popen.call_args[0][0][5], str(pixel_ratio))

    def test_windows_file_name(self):
        self.fake_popen.side_effect = Exception("Enough test. Abort")
        args = ["snapshot", "tests\\fixtures\\render.html", "jpeg", "0.1"]
        try:
            with patch.object(sys, "argv", args):
                main()
        except Exception:
            print(self.fake_popen.call_args)
            assert self.fake_popen.call_args[0][0][2].startswith("file:////")
            assert self.fake_popen.call_args[0][0][2].endswith(
                "tests/fixtures/render.html"
            )

    def test_default_delay_value(self):
        self.fake_popen.side_effect = CustomTestException("Enough test. Abort")
        args = ["snapshot", HTML_FILE, "jpeg"]
        try:
            with patch.object(sys, "argv", args):
                main()
        except CustomTestException:
            print(self.fake_popen.call_args)
            eq_(self.fake_popen.call_args[0][0][4], "1500")

    @raises(Exception)
    def test_unknown_file_type_at_command_line(self):
        self.fake_popen.return_value.stdout = BytesIO(get_base64_image())
        args = ["snapshot", HTML_FILE, "moonwalk"]
        with patch.object(sys, "argv", args):
            main()


@patch("subprocess.Popen")
@patch("pyecharts_snapshot.main.chk_phantomjs")
def test_make_png_snapshot(fake_check, fake_popen):
    fake_popen.return_value.stdout = BytesIO(get_base64_image())
    test_output = "custom.png"
    make_a_snapshot(get_fixture("render.html"), test_output)
    assert filecmp.cmp(test_output, get_fixture("sample.png"))


@patch("subprocess.Popen")
@patch("pyecharts_snapshot.main.chk_phantomjs")
def test_make_jpeg_snapshot(fake_check, fake_popen):
    fake_popen.return_value.stdout = BytesIO(get_base64_image())
    test_output = "custom.jpeg"
    make_a_snapshot(
        os.path.join("tests", "fixtures", "render.html"), test_output
    )
    assert filecmp.cmp(test_output, get_fixture("sample.jpeg"))


@raises(Exception)
@patch("subprocess.Popen")
@patch("pyecharts_snapshot.main.chk_phantomjs")
def test_phantomjs_fails(fake_check, fake_popen):
    fake_popen.return_value.stdout = BytesIO("abc")
    make_a_snapshot(
        os.path.join("tests", "fixtures", "render.html"), "custom.jpeg"
    )


@patch("subprocess.Popen")
@patch("pyecharts_snapshot.main.chk_phantomjs")
def test_win32_shell_flag(fake_check, fake_popen):
    fake_popen.side_effect = CustomTestException("Enough. Stop testing")
    try:
        with patch.object(sys, "platform", "win32"):
            make_a_snapshot(
                os.path.join("tests", "fixtures", "render.html"), "sample.png"
            )
    except CustomTestException:
        eq_(fake_popen.call_args[1]["shell"], True)


@patch("subprocess.Popen")
@patch("pyecharts_snapshot.main.chk_phantomjs")
def test_win32_shell_flag_is_false(fake_check, fake_popen):
    fake_popen.side_effect = CustomTestException("Enough. Stop testing")
    try:
        make_a_snapshot(
            os.path.join("tests", "fixtures", "render.html"), "sample.png"
        )
    except CustomTestException:
        eq_(fake_popen.call_args[1]["shell"], False)


def test_make_a_snapshot_real():
    # cannot produce a consistent binary matching file
    test_output = "real.png"
    make_a_snapshot(
        os.path.join("tests", "fixtures", "render.html"), test_output
    )
    assert os.path.exists(test_output)  # exists just fine


def test_svg_at_command_line():
    args = ["snapshot", SVG_HTML_FILE, "svg"]
    with patch.object(sys, "argv", args):
        main()
    assert os.path.exists("output.svg")


def test_save_svg():
    test_data = "<svg></svg>"
    outfile = "great.svg"
    save_as_svg(test_data, outfile)
    with codecs.open(outfile) as f:
        content = f.read()
        eq_(test_data, content)
    os.unlink(outfile)


def test_make_a_snapshot_real_pdf():
    test_output = "real.pdf"
    make_a_snapshot(
        os.path.join("tests", "fixtures", "render.html"), test_output
    )
    assert os.path.exists(test_output)  # exists just fine


@raises(TypeError)
def test_unsupported_file_type():
    # cannot produce a consistent binary matching file
    test_output = "real.shady"
    make_a_snapshot(
        os.path.join("tests", "fixtures", "render.html"), test_output
    )


def test_to_file_uri():
    windows_file = "C:\\user\\tmp.html"
    uri = to_file_uri(windows_file)
    eq_(uri, "file:///C:/user/tmp.html")
    linux_file = "tests/fixtures/tmp.html"
    uri2 = to_file_uri(linux_file)
    assert uri2.startswith("file:////")
    assert uri2.endswith(linux_file)


def get_base64_image():
    with open(get_fixture("base64.txt"), "r") as f:
        content = f.read().replace("\r\n", "")
        return ("," + content).encode("utf-8")


def get_fixture(name):
    return os.path.join("tests", "fixtures", name)
