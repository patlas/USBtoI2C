import serial

#  ser = serial.Serial(
#          port='/dev/ttyACM0',
#          baudrate=115200,
#          parity=serial.PARITY_NONE,
#          stopbits=serial.STOPBITS_ONE,
#          bytesize=serial.EIGHTBITS
#
#          )
#
#  print(ser.isOpen())
#
#  packet = bytearray()
#  packet.append(0x02)
#  packet.append(0x1C) #0x0E
#  packet.append(0x07)
#  packet.append(0x01)
#  packet.append(0xBB)
#
#  #  ser.write(packet)
#  #  thestring = "7E FF 03 00 01 00 02 0A 01 C8 04 D0 01 02 80 00 00 00 00 8E E7 7E"
#  #  data = struct.pack(hex(thestring))
#
#  ser.write(packet)
#  #  s = ser.read(5)
#  #  print(s)
#  s = ser.read(1)
#  print(s)
#  ser.close()
#


class SMBus:
    def __init__(self, ids):

        self.ser = serial.Serial(
                port='/dev/ttyACM1',
                baudrate=115200,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
                )

    def close(self):
        self.ser.close()

    def _prepare_data(self, cmd, addr, reg, size, data):
        packet = bytearray()
        if cmd == "WRITE":
            packet.append(0x01)

        else:
            packet.append(0x02)

        packet.append(addr<<1) #0x0E
        packet.append(reg)
        packet.append(size)

        if cmd == "WRITE":
            for i in range(size):
                packet.append(data[i])

        return packet

    

    def read_byte_data(self, dev_addr, reg_addr):
        data = self._prepare_data("READ", dev_addr, reg_addr, 1, None)
        self.ser.write(data)
        readout = self.ser.read(1)
        print(readout)
        return int.from_bytes(readout, "big")


    def write_byte_data(self, dev_addr, reg_addr, byte):
        data = self._prepare_data("WRITE", dev_addr, reg_addr, 1, [byte])
        print(data)
        self.ser.write(data)


    def read_i2c_block_data(self, dev_addr, reg_addr, count):
        data = self._prepare_data("READ", dev_addr, reg_addr, count, None)
        self.ser.write(data)
        readout = self.ser.read(count)
        print(readout)
        return [x for x in readout]

