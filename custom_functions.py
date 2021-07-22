import os
import sys
import json
from serial.tools.list_ports import comports


CONFIG_FILE = "config.json"  # Configuration file path


def get_config(path=CONFIG_FILE):
    """ Get Configurations JSON data """
    if not os.path.isfile(path):
        print(f"File not found [{path}]!")
        sys.exit(1)
    with open(path, 'r') as f:
        config = json.loads(f.read())
        return config


def get_port():
    """ Return Detected Ports """
    ports = []
    config = get_config()
    for port in comports():
        description = port.description.lower()
        for device, info in config["devices"].items():
            if device.lower() in description or description in info.lower():
                ports.append((port.device, info))
    return ports


if __name__ == '__main__':
    print(get_port())
