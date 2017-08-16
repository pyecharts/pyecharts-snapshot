import io
import os
import sys
import base64
import subprocess


PY2 = sys.version_info[0] == 2


def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'=' * (4 - missing_padding)
    return base64.decodestring(data)


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path


def main():
    file_name = sys.argv[1]
    make_a_snapshot(file_name, 'output.png')


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
    with open(output_name, "wb") as g:
        g.write(decode_base64(png.encode('utf-8')))
