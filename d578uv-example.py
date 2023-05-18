#!/usr/bin/env python
import serial
import time

class d578uv:
    #start_tx = [ 0x41, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06 ]
    start_tx = [ 0x41, 0x00, 0x01, 0x00, 0x1d, 0x00, 0x00 ]
    #stop_tx = [ 0x41, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06 ]
    stop_tx = [ 0x41, 0x00, 0x00, 0x01, 0x1d, 0x00, 0x00 ]

    ser = None

    def __init__(self, serial_port='COM4'):
        self.ser = serial.Serial(serial_port, 9600) #115200

    def _do_Tx(self):
        confirmation_byte = None
        while confirmation_byte != 'aa':
            self.ser.write(self.start_tx)
            buf_a = [ ]
            count = 0
            while '06' not in buf_a and count < 100:
                this_byte = self.ser.read(1).hex()
                buf_a.append(this_byte)
                if this_byte == 'aa':
                    confirmation_byte = 'aa'
                    break
                count += 1
            print(buf_a)

    def _do_Rx(self):
        confirmation_byte = None
        while confirmation_byte != 'aa':
            self.ser.write(self.stop_tx)
            buf_a = [ ]
            count = 0
            while '06' not in buf_a and count < 100:
                this_byte = self.ser.read(1).hex()
                buf_a.append(this_byte)
                if this_byte == 'aa':
                    confirmation_byte = 'aa'
                    break
                count += 1
            print(buf_a)

    def Tx(self, timeout=0):
        self._do_Tx()
        if timeout > 0:
            time.sleep(timeout)
            self._do_Rx()

    def Dump(self):
        while True:
            this_command = []
            count = 0
            while '06' not in this_command and 'aa' not in this_command and count < 100:
                this_byte = self.ser.read(1).hex()
                this_command.append(this_byte)
                count += 1
            print(this_command)
