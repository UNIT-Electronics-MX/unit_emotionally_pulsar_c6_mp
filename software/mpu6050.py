from machine import I2C
import time

class MPU6050:
    def __init__(self, i2c, addr=0x68):
        self.addr = addr
        self.i2c = i2c
        self.i2c.writeto_mem(self.addr, 0x6B, b'\x00')  # Despertar sensor

    def read_accel(self):
        data = self.i2c.readfrom_mem(self.addr, 0x3B, 6)
        acc_x = int.from_bytes(data[0:2], 'big', True)
        acc_y = int.from_bytes(data[2:4], 'big', True)
        acc_z = int.from_bytes(data[4:6], 'big', True)
        return (acc_x / 16384, acc_y / 16384, acc_z / 16384)

