import os
import sys
import json
import string
from serial.tools.list_ports import comports


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_ports():
    """ Return Detected Ports """
    ports = []
    for port in comports():
        description = port.description.lower()
        if description != 'n/a':
            ports.append({
                "product": port.product,
                "device": port.device})
    return ports


def dump_json(path, data):
    with open(path, 'w') as f:
        f.write(json.dumps(data, indent=4))


def load_json(path):
    with open(path, 'r') as f:
        return json.loads(f.read())


def good_chars():
    chars = string.printable
    for c in "*\t\n\r\x0b\x0c":
        chars = chars.replace(c, '')
    return chars


if __name__ == '__main__':
    print(get_ports())
