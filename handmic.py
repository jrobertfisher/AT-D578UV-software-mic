import serial
from tkinter import *

# Open the serial connection to the radio
#ser = serial.Serial('COM4', 9600, timeout=1)

# Function to change the zone on the radio
def change_zone(zone):
    # Open the serial connection to the radio
    ser = serial.Serial('COM4', 9600, timeout=1)
    # Send the appropriate commands to the radio to change the zone
    ser.write(b'\x01\x1f' + bytes([zone]) + b'\x0d\x0a')
    #ser.write(b'AT+ZONEUP\r\n')
    response = ser.readline().decode()
    # Wait for the response
    response = ser.readline().decode()
    # Close the serial port
    ser.close()
    # Print the response
    print(response.strip())



# Create the GUI
root = Tk()
root.title("Anytone UV-578 Zone Changer")

# Define the variable 'zone' with an initial value of 0
zone = IntVar(value=0)

# Add a label to the GUI
label = Label(root, text="Select the zone to change to:")
label.pack()

# Add some radio buttons to the GUI
zone1_button = Radiobutton(root, text="Zone 1", variable=zone, value=1)
zone2_button = Radiobutton(root, text="Zone 2", variable=zone, value=2)
zone3_button = Radiobutton(root, text="Zone 3", variable=zone, value=3)
zone1_button.pack()
zone2_button.pack()
zone3_button.pack()

# Add a button to trigger the zone changing function
button = Button(root, text="Change Zone", command=lambda: change_zone(zone.get()))
button.pack()

# Start the GUI main loop
root.mainloop()