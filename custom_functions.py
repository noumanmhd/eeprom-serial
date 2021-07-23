import string
from serial.tools.list_ports import comports


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


def good_chars():
    chars = string.printable
    for c in "*\t\n\r\x0b\x0c":
        chars = chars.replace(c, '')
    return chars


if __name__ == '__main__':
    print(get_ports())
