import smbus
class MCP4725:
    def __init__ (self,dynamic_range, address = 0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range
    
    
    def deinit(self):
        self.bus.close()

    def set_number(self,number):
        if not isinstance(number, int):
            print("На вход можно подавать только целые числа")

        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61,first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number} , отправленные I2c данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X} , 0x{second_byte:02X}]\n")
    def set_voltage(self,voltage):
        self.set_number(round(voltage/self.dynamic_range*4095))
if __name__ == "__main__":
    try:
        MCP = MCP4725(5 , True)
        while True:
            try:
                voltage = float (input("Введите напряжение в Вольтах: "))
                MCP.set_voltage(voltage)
            except ValueError:
                print("Вы не ввели число.Попробуйте езе раз")
    finally:
        MCP.deinit()