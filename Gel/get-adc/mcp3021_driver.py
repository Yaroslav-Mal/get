import smbus
import time
class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()
    
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2 )
        if self.verbose:
            print(f"Принятые данные: {data}, Старший Байт: {upper_data_byte: x}, Младший Байт: {lower_data_byte: x}, Число : {number}")
        return number
    
    def get_voltage(self):
        number = self.get_number()
        voltage = (number / 1024) * self.dynamic_range
        return voltage

if __name__ == "__main__":
    try:
        MCP = MCP3021(3.138, True)
        while True:
            voltage = MCP.get_voltage()
            print(voltage)
            time.sleep(0.01)

    finally:
        MCP.deinit()