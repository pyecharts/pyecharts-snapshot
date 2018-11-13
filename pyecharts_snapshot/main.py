import io
import os
import sys
import base64
import codecs
import subprocess

import pyecharts_snapshot.logger as logger

from PIL import Image

PY2 = sys.version_info[0] == 2

if PY2:
    from StringIO import StringIO as BytesIO
else:
    from io import BytesIO

HELP_TEXT = """
Usage:   snapshot input file [png|jpeg|gif|svg|pdf|eps] [delay] [pixel ratio]
         snapshot help: display this help message
Parameters:
         delay: float value, unit in seconds and defaults 1.5 seconds
         pixel ratio: integer value, defaults to 2
         document online:github.com/pyecharts/pyecharts-snapshot
"""

DEFAULT_DELAY = 1.5
DEFAULT_PIXEL_RATIO = 2
PNG_FORMAT = "png"
JPG_FORMAT = "jpeg"
GIF_FORMAT = "gif"
PDF_FORMAT = "pdf"
SVG_FORMAT = "svg"
EPS_FORMAT = "eps"

SUPPORTED_IMAGE_FORMATS = [
    PDF_FORMAT, JPG_FORMAT, GIF_FORMAT, SVG_FORMAT, EPS_FORMAT]

PHANTOMJS_EXEC = "phantomjs"
DEFAULT_OUTPUT_NAME = "output.%s"
NOT_SUPPORTED_FILE_TYPE = "Not supported file type '%s'"

MESSAGE_GENERATING = "Generating file ..."
MESSAGE_PHANTOMJS_VERSION = "phantomjs version: %s"
MESSAGE_FILE_SAVED_AS = "File saved in %s"
MESSAGE_NO_SNAPSHOT = (
    "No snapshot taken by phantomjs. "
    "Please make sure it is installed and available on your PATH!"
)
MESSAGE_NO_PHANTOMJS = "No phantomjs found in your PATH. Please install it!"


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 5:
        show_help()
    file_name = sys.argv[1]
    if file_name == "help":
        show_help()
    delay = DEFAULT_DELAY
    output = DEFAULT_OUTPUT_NAME % PNG_FORMAT
    pixel_ratio = DEFAULT_PIXEL_RATIO
    if len(sys.argv) >= 3:
        file_type = sys.argv[2]
        if file_type in SUPPORTED_IMAGE_FORMATS:
            output = DEFAULT_OUTPUT_NAME % file_type
        elif file_type != PNG_FORMAT:
            raise TypeError(NOT_SUPPORTED_FILE_TYPE % file_type)
        if len(sys.argv) >= 4:
            delay = float(sys.argv[3])  # in seconds
            if len(sys.argv) == 5:
                pixel_ratio = sys.argv[4]
    make_a_snapshot(file_name, output, delay=delay, pixel_ratio=pixel_ratio)


def show_help():
    logger.info(HELP_TEXT)
    exit(0)


def make_a_snapshot(
    file_name,
    output_name,
    delay=DEFAULT_DELAY,
    pixel_ratio=DEFAULT_PIXEL_RATIO,
    verbose=True,
):
    chk_phantomjs()
    logger.VERBOSE = verbose
    logger.info(MESSAGE_GENERATING)
    file_type = output_name.split(".")[-1]
    __actual_delay_in_ms = int(delay * 1000)
    # add shell=True and it works on Windows now.
    proc_params = [
        PHANTOMJS_EXEC,
        os.path.join(get_resource_dir("phantomjs"), "snapshot.js"),
        to_file_uri(file_name),
        file_type,
        str(__actual_delay_in_ms),
        str(pixel_ratio),
    ]
    proc = subprocess.Popen(
        proc_params,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=get_shell_flag(),
    )
    if PY2:
        content = proc.stdout.read()
        content = content.decode("utf-8")
    else:
        content = io.TextIOWrapper(proc.stdout, encoding="utf-8").read()
    if file_type == SVG_FORMAT:
        save_as_svg(content, output_name)
    else:
        # pdf, gif, png, jpeg
        content_array = content.split(",")
        if len(content_array) != 2:
            raise OSError(content_array)
        base64_imagedata = content_array[1]
        imagedata = decode_base64(base64_imagedata)
        if file_type in [PDF_FORMAT, GIF_FORMAT, EPS_FORMAT]:
            save_as(imagedata, output_name, file_type)
        elif file_type in [PNG_FORMAT, JPG_FORMAT]:
            save_as_png(imagedata, output_name)
        else:
            raise TypeError(NOT_SUPPORTED_FILE_TYPE.format(file_type))
    if "/" not in output_name:
        output_name = os.path.join(os.getcwd(), output_name)

    logger.info(MESSAGE_FILE_SAVED_AS % output_name)


def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += "=" * (4 - missing_padding)
    return base64.decodestring(data.encode("utf-8"))


def save_as_png(imagedata, output_name):
    with open(output_name, "wb") as f:
        f.write(imagedata)


def save_as_svg(imagedata, output_name):
    with codecs.open(output_name, "w", encoding="utf-8") as f:
        f.write(imagedata)


def save_as(imagedata, output_name, file_type):
    m = Image.open(BytesIO(imagedata))
    m.load()
    color = (255, 255, 255)
    b = Image.new("RGB", m.size, color)
    b.paste(m, mask=m.split()[3])
    b.save(output_name, file_type, quality=100)


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path


def chk_phantomjs():
    try:
        phantomjs_version = subprocess.check_output(
            [PHANTOMJS_EXEC, "--version"], shell=get_shell_flag()
        )
        phantomjs_version = phantomjs_version.decode("utf-8")
        logger.info(MESSAGE_PHANTOMJS_VERSION % phantomjs_version)
    except Exception:
        logger.warn(MESSAGE_NO_PHANTOMJS)
        sys.exit(1)


def get_shell_flag():
    return sys.platform == "win32"


def to_file_uri(a_file_name):
    __universal_file_name = a_file_name.replace("\\", "/")
    if ":" not in a_file_name:
        __universal_file_name = os.path.abspath(__universal_file_name)
    return "file:///{0}".format(__universal_file_name)
