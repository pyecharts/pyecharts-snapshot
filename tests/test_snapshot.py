import os
import sys
import codecs
import filecmp
from asyncio import coroutine

from pyecharts_snapshot.main import (
    SNAPSHOT_JS,
    main,
    to_file_uri,
    save_as_text,
    make_a_snapshot,
)

from mock import Mock, patch
from nose.tools import eq_, raises
from aiounittest import async_test

HTML_FILE = os.path.join("tests", "fixtures", "render.html")
SVG_HTML_FILE = os.path.join("tests", "fixtures", "render_svg_cangzhou.html")


class CustomTestException(Exception):
    pass


class TestMain:
    def setUp(self):
        def CoroMock():
            coro = Mock(return_value=get_base64_image())
            corofunc = Mock(
                name="CoroutineFunction", side_effect=coroutine(coro)
            )
            corofunc.coro = coro
            return corofunc

        self.patcher = patch(
            "pyecharts_snapshot.main.get_echarts", new_callable=CoroMock
        )
        self.fake_popen = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    @raises(SystemExit)
    def test_no_params(self):
        args = ["snapshot"]
        with patch.object(sys, "argv", args):
            main()

    @raises(TypeError)
    def test_unsupported_file_type(self):
        args = ["snapshot", "real.html", "shady"]
        with patch.object(sys, "argv", args):
            main()

    @raises(SystemExit)
    def test_help(self):
        args = ["snapshot", "help"]
        with patch.object(sys, "argv", args):
            main()

    def test_main(self):
        args = ["snapshot", HTML_FILE]
        with patch.object(sys, "argv", args):
            main()
            assert filecmp.cmp("output.png", get_fixture("sample.png"))

    def test_jpeg_at_command_line(self):
        args = ["snapshot", HTML_FILE, "jpeg"]
        with patch.object(sys, "argv", args):
            main()
        assert filecmp.cmp("output.jpeg", get_fixture("sample.jpeg"))

    def test_pdf_at_command_line(self):
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
            expected = SNAPSHOT_JS % ("jpeg", 2, 100)
            eq_(self.fake_popen.call_args[0][1], expected)

    def test_pixel_option(self):
        self.fake_popen.side_effect = Exception("Enough test. Abort")
        pixel_ratio = 5
        args = ["snapshot", HTML_FILE, "jpeg", "0.1", str(pixel_ratio)]
        try:
            with patch.object(sys, "argv", args):
                main()
        except Exception:
            expected = SNAPSHOT_JS % ("jpeg", pixel_ratio, 100)
            eq_(self.fake_popen.call_args[0][1], expected)

    def test_windows_file_name(self):
        self.fake_popen.side_effect = Exception("Enough test. Abort")
        args = ["snapshot", "tests\\fixtures\\render.html", "jpeg", "0.1"]
        try:
            with patch.object(sys, "argv", args):
                main()
        except Exception:
            print(self.fake_popen.call_args[0][0])
            assert self.fake_popen.call_args[0][0].startswith("file:///")
            assert self.fake_popen.call_args[0][0].endswith(
                os.path.join("tests", "fixtures", "render.html")
            )

    def test_default_delay_value(self):
        self.fake_popen.side_effect = CustomTestException("Enough test. Abort")
        args = ["snapshot", HTML_FILE, "jpeg"]
        try:
            with patch.object(sys, "argv", args):
                main()
        except CustomTestException:
            expected = SNAPSHOT_JS % ("jpeg", 2, 1500)
            eq_(self.fake_popen.call_args[0][1], expected)

    @raises(Exception)
    def test_unknown_file_type_at_command_line(self):
        args = ["snapshot", HTML_FILE, "moonwalk"]
        with patch.object(sys, "argv", args):
            main()


@async_test
async def test_make_png_snapshot():
    def CoroMock():
        coro = Mock(return_value=get_base64_image())
        corofunc = Mock(name="CoroutineFunction", side_effect=coroutine(coro))
        corofunc.coro = coro
        return corofunc

    with patch("pyecharts_snapshot.main.get_echarts", new_callable=CoroMock):
        test_output = "custom.png"
        await make_a_snapshot(get_fixture("render.html"), test_output)
        assert filecmp.cmp(test_output, get_fixture("sample.png"))


@async_test
async def test_make_jpeg_snapshot():
    def CoroMock():
        coro = Mock(return_value=get_base64_image())
        corofunc = Mock(name="CoroutineFunction", side_effect=coroutine(coro))
        corofunc.coro = coro
        return corofunc

    with patch("pyecharts_snapshot.main.get_echarts", new_callable=CoroMock):
        test_output = "custom.jpeg"
        await make_a_snapshot(
            os.path.join("tests", "fixtures", "render.html"), test_output
        )
        assert filecmp.cmp(test_output, get_fixture("sample.jpeg"))


@raises(Exception)
@async_test
async def test_phantomjs_fails(fake_check, fake_popen):
    def CoroMock():
        coro = Mock(return_value="abc")
        corofunc = Mock(name="CoroutineFunction", side_effect=coroutine(coro))
        corofunc.coro = coro
        return corofunc

    with patch("pyecharts_snapshot.main.get_echarts", new_callable=CoroMock):
        await make_a_snapshot(
            os.path.join("tests", "fixtures", "render.html"), "custom.jpeg"
        )


@async_test
async def test_win32_shell_flag_is_false_for_non_win32_os():
    def CoroMock():
        coro = Mock(return_value="abc")
        corofunc = Mock(
            name="CoroutineFunction",
            side_effect=CustomTestException("Enough. Stop testing"),
        )
        corofunc.coro = coro
        return corofunc

    with patch(
        "pyecharts_snapshot.main.get_echarts", new_callable=CoroMock
    ) as p:
        try:
            await make_a_snapshot(
                os.path.join("tests", "fixtures", "render.html"), "sample.png"
            )
        except CustomTestException:
            p.assert_called()


@async_test
async def test_make_a_snapshot_real():
    # cannot produce a consistent binary matching file
    test_output = "real.png"
    await make_a_snapshot(
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
    save_as_text(test_data, outfile)
    with codecs.open(outfile) as f:
        content = f.read()
        eq_(test_data, content)
    os.unlink(outfile)


@async_test
async def test_make_a_snapshot_real_pdf():
    test_output = "real.pdf"
    await make_a_snapshot(
        os.path.join("tests", "fixtures", "render.html"), test_output
    )
    assert os.path.exists(test_output)  # exists just fine


def test_to_file_uri():
    windows_file = "C:\\user\\tmp.html"
    uri = to_file_uri(windows_file)
    eq_(uri, "file:///C:/user/tmp.html")
    linux_file = os.path.join("tests", "fixtures", "tmp.html")
    uri2 = to_file_uri(linux_file)
    assert uri2.startswith("file:///")
    assert uri2.endswith(linux_file)


def get_base64_image():
    with open(get_fixture("base64.txt"), "r") as f:
        content = f.read().replace("\r\n", "")
        return "," + content


def get_fixture(name):
    return os.path.join("tests", "fixtures", name)
