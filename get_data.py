import json
import serial

RETRIES = 5
MEMORY_LIMIT = 2048

DEBUG = False


class SerialData:
    def __init__(self, port='/dev/ttyUSB0', baud=9600):
        self.ser = serial.Serial(port, baud, timeout=1)

    def get_data(self):
        for _ in range(RETRIES):
            data = self.ser.readline()
            try:
                data = data.decode(encoding="utf-8")
                data = json.loads(data)
                return data
            except:
                pass
        return None

    def update(self, addr, value):
        addr = abs(int(addr))
        value = abs(int(value))
        cmd = f"P{addr:04X}{value:04X}\n".encode('utf-8')
        for _ in range(RETRIES):
            self.ser.write(cmd)
            data = self.get_data()
            if isinstance(data, dict):
                if data['status']:
                    if DEBUG:
                        print(
                            f"Addr: 0x{addr:04X}, Value: {value:04X}, Status: True")
                    return None

    def get(self, addr):
        addr = abs(int(addr))
        cmd = f"G{addr:04X}{0:04X}\n".encode('utf-8')
        for _ in range(RETRIES):
            self.ser.write(cmd)
            data = self.get_data()
            if isinstance(data, dict):
                if data['status']:
                    if DEBUG:
                        print(data)
                    return data['value']
        return False

    def get_ref(self, ref_addr, addr):
        addr = abs(int(addr))
        ref_addr = abs(int(ref_addr))
        current_addr = ref_addr + addr
        return self.get(current_addr)

    def update_ref(self, ref_addr, addr, value):
        addr = abs(int(addr))
        ref_addr = abs(int(ref_addr))
        current_addr = ref_addr + addr
        return self.update(current_addr, value)

    def clear(self):
        for addr in range(MEMORY_LIMIT):
            self.update(addr, 0)

    def dump(self, path):
        data = {}
        for addr in range(MEMORY_LIMIT):
            data[f"0x{addr:04X}"] = self.get(addr)
        with open(path, 'w') as f:
            f.write(json.dumps(data, indent=4))

    def close(self):
        self.ser.close()

    def __del__(self):
        self.ser.close()


if __name__ == '__main__':
    ser = SerialData()
    # ser.clear()
    # ser.update(0,2)
    # ser.get(5)
    ser.dump('dump.json')
    ser.close()
