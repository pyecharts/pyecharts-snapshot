import io
import base64
import subprocess


def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'=' * (4 - missing_padding)
    return base64.decodestring(data)


def main():
    proc = subprocess.Popen(['phantomjs', 'gen.js'], stdout=subprocess.PIPE)
    content = io.TextIOWrapper(proc.stdout, encoding="utf-8").read()
    print(content)
    png = content.split(',')[1]
    with open("out.png", "wb") as g:
        g.write(decode_base64(png.encode('utf-8')))
