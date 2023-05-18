# import serial

# ser = serial.Serial('COM4', 9600, timeout=1)
# ser.write(b'ATI\r\n')
# response = ser.readline().decode()
# ser.close()

import tkinter as tk
import serial

Baudrate = 9600
#Baudrate = 115200

class SerialGUI:
    def __init__(self, master):
        self.master = master
        master.title("Serial GUI")

        # Create a serial object and open the serial port
        self.ser = serial.Serial('COM4', Baudrate, timeout=1)
        self.ser.flushInput()

        # Create a text box to display received data
        self.textbox = tk.Text(master, width=50, height=10)
        self.textbox.pack()

        # Create an entry box for sending data
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Create a button to send data
        self.send_button = tk.Button(master, text="Send", command=self.send_data)
        self.send_button.pack()

        # Set up a loop to continuously read data from the serial port
        self.read_serial()

    def send_data(self):
        # Get the data from the entry box and send it over the serial port
        #data = self.entry.get()
        #self.ser.write(data.encode())

        # Get the data from the entry box as a string of hex values
        hex_string = self.entry.get()

        # Convert the hex string to a bytes object
        data = bytes.fromhex(hex_string)

        # Send the data over the serial port
        self.ser.write(data)

    def read_serial(self):
        # Read data from the serial port and display it in the text box
        if self.ser.in_waiting > 0:
            #data = self.ser.readline().decode().rstrip()
            #data = self.ser.readline().decode(errors='replace').rstrip()
            data = self.ser.readline().decode('cp1252').rstrip()
            self.textbox.insert(tk.END, data + '\n')
        self.master.after(100, self.read_serial)

root = tk.Tk()
gui = SerialGUI(root)
root.mainloop()