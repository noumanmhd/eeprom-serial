from serial.tools.list_ports import comports

def get_port():
    """ Return Detected Ports """
    ports = []
    for port in comports():
        description = port.description.lower()
        if description != 'n/a':
            ports.append((port.product, port.device))
    return ports


if __name__ == '__main__':
    print(get_port())
