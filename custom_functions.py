from serial.tools.list_ports import comports
from get_data import SerialData

def serial_get(port, addr):
    ser = SerialData(port=port)
    value = ser.get(addr)
    del ser
    return value

def serial_get_ref(port, ref_addr, addr):
    addr = abs(int(addr))
    ref_addr = abs(int(ref_addr))
    current_addr = ref_addr + addr
    return serial_get(port, current_addr)

def serial_update(port, addr, value):
    ser = SerialData(port=port)
    ser.update(addr, value)
    del ser

def serial_update_ref(port, ref_addr, addr, value):
    addr = abs(int(addr))
    ref_addr = abs(int(ref_addr))
    current_addr = ref_addr + addr
    return serial_update(port, current_addr, value)

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


if __name__ == '__main__':
    print(get_ports())
