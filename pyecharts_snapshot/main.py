import io
import os
import sys
import base64
import subprocess
from PIL import Image


PY2 = sys.version_info[0] == 2

if PY2:
    from StringIO import StringIO as BytesIO
else:
    from io import BytesIO

NOT_SUPPORTED_FILE_TYPE = "Do not support file type %s"


def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        output = 'output.png'
        if len(sys.argv) == 3:
            file_type = sys.argv[2]
            if file_type == 'pdf':
                output = 'output.pdf'
            elif file_type != 'png':
                raise Exception(NOT_SUPPORTED_FILE_TYPE % file_type)
        make_a_snapshot(file_name, output)


def make_a_snapshot(file_name, output_name):
    proc = subprocess.Popen(
        ['phantomjs',
         os.path.join(get_resource_dir('phantomjs'), 'snapshot.js'),
         file_name], stdout=subprocess.PIPE)
    if PY2:
        content = proc.stdout.read()
        content = content.decode('utf-8')
    else:
        content = io.TextIOWrapper(proc.stdout, encoding="utf-8").read()
    png = content.split(',')[1]
    imagedata = decode_base64(png.encode('utf-8'))
    file_type = output_name.split('.')[-1]
    if file_type == 'pdf':
        save_as_pdf(imagedata, output_name)
    elif file_type == 'png':
        save_as_png(imagedata, output_name)
    else:
        raise Exception(NOT_SUPPORTED_FILE_TYPE % file_type)


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
    with open(output_name, "wb") as g:
        g.write(imagedata)


def save_as_pdf(imagedata, output_name):
    m = Image.open(BytesIO(imagedata))
    m.load()
    color = (255, 255, 255)
    b = Image.new('RGB', m.size, color)
    b.paste(m, mask=m.split()[3])
    b.save(output_name, 'PDF', quality=100)


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path
