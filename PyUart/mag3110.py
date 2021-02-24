from Driver import Driver
import uart as smbus
import time

class Mag3110Driver(Driver):
    DEV_ADDR = 0x0E
    REG_DR_STATUS = 0x00
    REG_WHO_AM_I = 0x07
    REG_TEMP = 0x0F
    REG_SYSMOD = 0x08
    REG_CTRL_REG1 = 0x10
    REG_CTRL_REG2 = 0x11

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.bus.close()
        except:
            pass

    def __init__(self, i2c_id:int, supply_type:str, read_freq=40):
        self.name = "MAG3110"#_{}".format(supply_type)
        self.bus = smbus.SMBus(i2c_id)
        time.sleep(1)

        status = self.bus.read_byte_data(self.DEV_ADDR, self.REG_WHO_AM_I)
        if status == 0xC4: # 0xC4
            self.bus.write_byte_data(self.DEV_ADDR, self.REG_SYSMOD, 0x01) # set 40Hz aquisition, 16b resolution, automatic trigger data, raw mode 
            self.bus.write_byte_data(self.DEV_ADDR, self.REG_CTRL_REG1, 0x09) # set 40Hz aquisition, 16b resolution, automatic trigger data, raw mode 
            self.bus.write_byte_data(self.DEV_ADDR, self.REG_CTRL_REG2, 0xA0)
        else:
            raise Exception("Cannot connect to device, wrong ID={} expected 0xC4".format(hex(status)))

    def getMeasurement(self, readTemp=False):
        measurement = []
        while True:
            if (self.bus.read_byte_data(self.DEV_ADDR, self.REG_DR_STATUS) & 0x08) == 0x08:
                break
            
        data = self.bus.read_i2c_block_data(self.DEV_ADDR, 0x01, 6)
        for i in [0,2,4]:
            value = ((data[i]<<8 & 0xFF00)|data[i+1])
            if value > 32767:
                value -= 65536
            measurement.append(value)

        if readTemp:
            temp = self.bus.read_byte_data(self.DEV_ADDR, self.REG_TEMP)
            measurement.append(temp)

        return measurement

    def scaleMeasurement(self, measurement):
        return [m/20 for m in measurement]
