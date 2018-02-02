import io
import os
import sys
import base64
from PIL import Image
import subprocess

PY2 = sys.version_info[0] == 2

if PY2:
    from StringIO import StringIO as BytesIO
else:
    from io import BytesIO

PHANTOMJS_EXEC = "phantomjs"
NOT_SUPPORTED_FILE_TYPE = "Not supported file type '%s'"
DEFAULT_DELAY = 1.5
HELP= '''Usage:   snapshot {input file} {output type:[png|jpeg|gif|pdf]} {delay in seconds}
         snapshot help: display this help message
         snapshot help online: document online.'''

def main():
    if len(sys.argv) < 2:
        print('snapshot help')
        sys.exit(0)
    else:
        if sys.argv[1] == 'help':
            try:
                online = sys.argv[2]
                if online=='online':
                 print('https://github.com/pyecharts/pyecharts-snapshot')
                 sys.exit(0)
                else:
                    raise Exception
            except Exception:
                print(HELP)
                sys.exit(0)
        else:
            pass

    file_name = sys.argv[1]
    delay = DEFAULT_DELAY
    output = 'output.png'
    if len(sys.argv) >= 3:
        file_type = sys.argv[2]
        if file_type in ['pdf', 'jpeg', 'gif']:
            output = 'output.%s' % (file_type)
        elif file_type != 'png':
            raise TypeError(NOT_SUPPORTED_FILE_TYPE % file_type)
        if len(sys.argv) == 4:
            delay = float(sys.argv[3])  # in seconds
    chk_phantomjs()
    make_a_snapshot(file_name, output, delay=delay)


def make_a_snapshot(file_name, output_name, delay=DEFAULT_DELAY):
    print('Generating file ...')
    file_type = output_name.split('.')[-1]
    pixel_ratio = 2
    shell_flag = False
    if sys.platform == 'win32':
        shell_flag = True
    __actual_delay_in_ms = int(delay * 1000)

    # add shell=True and it works on Windows now.
    proc_params = [
        PHANTOMJS_EXEC,
        os.path.join(get_resource_dir('phantomjs'), 'snapshot.js'),
        file_name.replace('\\', '/'),
        file_type,
        str(__actual_delay_in_ms),
        str(pixel_ratio)
    ]
    print(proc_params)
    proc = subprocess.Popen(
        proc_params, stdout=subprocess.PIPE, shell=shell_flag)
    if PY2:
        content = proc.stdout.read()
        content = content.decode('utf-8')
    else:
        content = io.TextIOWrapper(proc.stdout, encoding="utf-8").read()
    content_array = content.split(',')
    print(content_array)
    if len(content_array) != 2:
        raise OSError(
            "No snapshot taken by phantomjs. "
            "Please make sure it is installed and available on your PATH!")
    base64_imagedata = content_array[1]
    imagedata = decode_base64(base64_imagedata.encode('utf-8'))
    if file_type in ['pdf', 'gif']:
        save_as(imagedata, output_name, file_type)
    elif file_type in ['png', 'jpeg']:
        save_as_png(imagedata, output_name)
    else:
        raise TypeError(NOT_SUPPORTED_FILE_TYPE.format(file_type))


def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'=' * (4 - missing_padding)
    return base64.decodestring(data)


def save_as_png(imagedata, output_name):
    with open(output_name, "wb") as f:
        f.write(imagedata)
    print('File rendered in ' + os.getcwd() + '/' + output_name)


def save_as(imagedata, output_name, file_type):
    m = Image.open(BytesIO(imagedata))
    m.load()
    color = (255, 255, 255)
    b = Image.new('RGB', m.size, color)
    b.paste(m, mask=m.split()[3])
    b.save(output_name, file_type, quality=100)
    print('File saved in %s/%s' % (os.getcwd(), output_name))


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    print(current_path)
    resource_path = os.path.join(current_path, folder)
    return resource_path


def chk_phantomjs():
    try:
        PHANTOMJS_VERSION = (
            subprocess.check_output([PHANTOMJS_EXEC, '--version'])).decode(
            'utf8')
        print("\nphantomjs version: %s" % PHANTOMJS_VERSION)
    except Exception:
        print("No phantomjs found in your PATH. Please install it!")
        sys.exit(0)