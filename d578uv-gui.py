#Copyright 2023 Rob Fisher
#Free for public use.

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import os
import serial
import time
import threading
from datetime import datetime


# Configure callsign
callsign = "KI5QPY"
# Configure the serial port
port = 'COM4'  # Replace with the appropriate port for your system
baud_rate = 115200  # Set the baud rate to 115200
timeout = 1  # Timeout in seconds
parity = serial.PARITY_NONE
stopbits=serial.STOPBITS_ONE
bytesize = serial.EIGHTBITS

# Open the serial port
ser = serial.Serial(port, baud_rate, timeout=timeout, parity=parity, stopbits=stopbits, bytesize=bytesize)

# Create a threading event to signal when to stop the thread
stop_event = threading.Event()
ser_stop_event = threading.Event()
Button_A_stop_event = threading.Event()
ptt_stop_event = threading.Event()

# for file in os.listdir('.'):
#     print(file)

# GUI Window
window = tk.Tk()
window.title("Handmic Emulator - Anytone AT-D578UVIII")
window.geometry("400x600")
window.resizable(False,False)

# Mic Image
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "AT-D578UVIII.png")
image = Image.open(image_path)
resized_image = image.resize((303, 578), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(resized_image)
background_label = tk.Label(window, image=tk_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Callsign overlay
label = tk.Label(window, text=callsign, font=("Arial", 19, "bold italic"), foreground="white", background="#262626", padx=0, pady=0)
label.place(x=155,y=72)

## Button PTT
# Define the command values for click and release
COMMAND_CLICK = b'\x41\x01\x00\x00\x00\x00\x00\x06'
COMMAND_RELEASE = b'\x41\x00\x00\x00\x00\x00\x00\x06'

last_button_press_time = None
double_click_interval = 1  # Set the desired interval for double clicks (in seconds)

def Button_PTT_thread():
    if ptt_stop_event.is_set():
        return

    # Send the click command
    ser.write(COMMAND_CLICK)
    print(f"Sent: {COMMAND_CLICK.hex()}")
    red_light.configure(bg="#FF0023") #Red

    # Read the response
    Button_PTT_Press_Response = ser.read()
    if len(Button_PTT_Press_Response) > 0:
        print(f"Response: {Button_PTT_Press_Response.hex()}")
    else:
        print("No response received")

def Button_PTT_release():
    if ptt_stop_event.is_set():
        return

    # Send the release command
    ser.write(COMMAND_RELEASE)
    print(f"Sent: {COMMAND_RELEASE.hex()}")
    red_light.configure(bg="#00C800") #Green

    # Read the response
    Button_PTT_Release_Response = ser.read()
    if len(Button_PTT_Release_Response) > 0:
        print(f"Response: {Button_PTT_Release_Response.hex()}")
    else:
        print("No response received")

def is_double_click():
    global last_button_press_time

    current_time = datetime.now()
    if last_button_press_time is None:
        last_button_press_time = current_time
        return False

    elapsed_time = (current_time - last_button_press_time).total_seconds()
    if elapsed_time <= double_click_interval:
        last_button_press_time = None
        return True

    last_button_press_time = current_time
    return False

button_PTT_thread = None

def start_Button_PTT_thread():
    global button_PTT_thread
    if not button_PTT_thread or not button_PTT_thread.is_alive():
        button_PTT_thread = threading.Thread(target=Button_PTT_thread)
        button_PTT_thread.start()

def stop_Button_PTT_thread():
    if button_PTT_thread and button_PTT_thread.is_alive():
        ptt_stop_event.set()
        button_PTT_thread.join()

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "button_ptt.png")
button_ptt_image = Image.open(image_path)
resize_button_ptt = button_ptt_image.resize((59, 71), Image.ANTIALIAS)
button_ptt = ImageTk.PhotoImage(resize_button_ptt)

def PTTButton_on_button_press(event):
    if not is_double_click():
        start_Button_PTT_thread()

def PTTButton_on_button_release(event):
    stop_Button_PTT_thread()
    Button_PTT_release()

# Create a custom button class that handles the mouse events
class PTTButton(tk.Button):
    def __init__(self, master=None, text=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Button-1>", PTTButton_on_button_press)
        self.bind("<ButtonRelease-1>", PTTButton_on_button_release)

## Button 0
def Button_0_thread():
    Button_0_values = [b'\x41\x00\x01\x00\x01\x00\x00\x06', b'\x41\x00\x00\x00\x01\x00\x00\x06']
    for Button_0_Press in Button_0_values:
        if stop_event.is_set():
            break
        ser.write(Button_0_Press)
        print(f"Sent: {Button_0_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_0_Press_Response = ser.read()
        if len(Button_0_Press_Response) > 0:
            print(f"Response: {Button_0_Press_Response.hex()}")
        else:
            print("No response received")

button_0_thread = None

def start_Button_0_thread():
    global button_0_thread
    if not button_0_thread or not button_0_thread.is_alive():
        button_0_thread = threading.Thread(target=Button_0_thread)
        button_0_thread.start()

def stop_Button_0_thread():
    if button_0_thread and button_0_thread.is_alive():
        stop_event.set()
        button_0_thread.join()

## Button 1
def Button_1_thread():
    Button_1_values = [b'\x41\x00\x01\x00\x02\x00\x00\x06', b'\x41\x00\x00\x00\x02\x00\x00\x06']
    for Button_1_Press in Button_1_values:
        if stop_event.is_set():
            break
        ser.write(Button_1_Press)
        print(f"Sent: {Button_1_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_1_Press_Response = ser.read()
        if len(Button_1_Press_Response) > 0:
            print(f"Response: {Button_1_Press_Response.hex()}")
        else:
            print("No response received")

button_1_thread = None

def start_Button_1_thread():
    global button_1_thread
    if not button_1_thread or not button_1_thread.is_alive():
        button_1_thread = threading.Thread(target=Button_1_thread)
        button_1_thread.start()

def stop_Button_1_thread():
    if button_1_thread and button_1_thread.is_alive():
        stop_event.set()
        button_1_thread.join()

## Button 2
def Button_2_thread():
    Button_2_values = [b'\x41\x00\x01\x00\x03\x00\x00\x06', b'\x41\x00\x00\x00\x03\x00\x00\x06']
    for Button_2_Press in Button_2_values:
        if stop_event.is_set():
            break
        ser.write(Button_2_Press)
        print(f"Sent: {Button_2_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_2_Press_Response = ser.read()
        if len(Button_2_Press_Response) > 0:
            print(f"Response: {Button_2_Press_Response.hex()}")
        else:
            print("No response received")

button_2_thread = None

def start_Button_2_thread():
    global button_2_thread
    if not button_2_thread or not button_2_thread.is_alive():
        button_2_thread = threading.Thread(target=Button_2_thread)
        button_2_thread.start()

def stop_Button_2_thread():
    if button_2_thread and button_2_thread.is_alive():
        stop_event.set()
        button_2_thread.join()

## Button 3
def Button_3_thread():
    Button_3_values = [b'\x41\x00\x01\x00\x04\x00\x00\x06', b'\x41\x00\x00\x00\x04\x00\x00\x06']
    for Button_3_Press in Button_3_values:
        if stop_event.is_set():
            break
        ser.write(Button_3_Press)
        print(f"Sent: {Button_3_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_3_Press_Response = ser.read()
        if len(Button_3_Press_Response) > 0:
            print(f"Response: {Button_3_Press_Response.hex()}")
        else:
            print("No response received")

button_3_thread = None

def start_Button_3_thread():
    global button_3_thread
    if not button_3_thread or not button_3_thread.is_alive():
        button_3_thread = threading.Thread(target=Button_3_thread)
        button_3_thread.start()

def stop_Button_3_thread():
    if button_3_thread and button_3_thread.is_alive():
        stop_event.set()
        button_3_thread.join()

## Button 4
def Button_4_thread():
    Button_4_values = [b'\x41\x00\x01\x00\x05\x00\x00\x06', b'\x41\x00\x00\x00\x05\x00\x00\x06']
    for Button_4_Press in Button_4_values:
        if stop_event.is_set():
            break
        ser.write(Button_4_Press)
        print(f"Sent: {Button_4_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_4_Press_Response = ser.read()
        if len(Button_4_Press_Response) > 0:
            print(f"Response: {Button_4_Press_Response.hex()}")
        else:
            print("No response received")

button_4_thread = None

def start_Button_4_thread():
    global button_4_thread
    if not button_4_thread or not button_4_thread.is_alive():
        button_4_thread = threading.Thread(target=Button_4_thread)
        button_4_thread.start()

def stop_Button_4_thread():
    if button_4_thread and button_4_thread.is_alive():
        stop_event.set()
        button_4_thread.join()

## Button 5
def Button_5_thread():
    Button_5_values = [b'\x41\x00\x01\x00\x06\x00\x00\x06', b'\x41\x00\x00\x00\x06\x00\x00\x06']
    for Button_5_Press in Button_5_values:
        if stop_event.is_set():
            break
        ser.write(Button_5_Press)
        print(f"Sent: {Button_5_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_5_Press_Response = ser.read()
        if len(Button_5_Press_Response) > 0:
            print(f"Response: {Button_5_Press_Response.hex()}")
        else:
            print("No response received")

button_5_thread = None

def start_Button_5_thread():
    global button_5_thread
    if not button_5_thread or not button_5_thread.is_alive():
        button_5_thread = threading.Thread(target=Button_5_thread)
        button_5_thread.start()

def stop_Button_5_thread():
    if button_5_thread and button_5_thread.is_alive():
        stop_event.set()
        button_5_thread.join()

## Button 6
def Button_6_thread():
    Button_6_values = [b'\x41\x00\x01\x00\x07\x00\x00\x06', b'\x41\x00\x00\x00\x07\x00\x00\x06']
    for Button_6_Press in Button_6_values:
        if stop_event.is_set():
            break
        ser.write(Button_6_Press)
        print(f"Sent: {Button_6_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_6_Press_Response = ser.read()
        if len(Button_6_Press_Response) > 0:
            print(f"Response: {Button_6_Press_Response.hex()}")
        else:
            print("No response received")

button_6_thread = None

def start_Button_6_thread():
    global button_6_thread
    if not button_6_thread or not button_6_thread.is_alive():
        button_6_thread = threading.Thread(target=Button_6_thread)
        button_6_thread.start()

def stop_Button_6_thread():
    if button_6_thread and button_6_thread.is_alive():
        stop_event.set()
        button_6_thread.join()

## Button 7
def Button_7_thread():
    Button_7_values = [b'\x41\x00\x01\x00\x08\x00\x00\x06', b'\x41\x00\x00\x00\x08\x00\x00\x06']
    for Button_7_Press in Button_7_values:
        if stop_event.is_set():
            break
        ser.write(Button_7_Press)
        print(f"Sent: {Button_7_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_7_Press_Response = ser.read()
        if len(Button_7_Press_Response) > 0:
            print(f"Response: {Button_7_Press_Response.hex()}")
        else:
            print("No response received")

button_7_thread = None

def start_Button_7_thread():
    global button_7_thread
    if not button_7_thread or not button_7_thread.is_alive():
        button_7_thread = threading.Thread(target=Button_7_thread)
        button_7_thread.start()

def stop_Button_7_thread():
    if button_7_thread and button_7_thread.is_alive():
        stop_event.set()
        button_7_thread.join()

## Button 8
def Button_8_thread():
    Button_8_values = [b'\x41\x00\x01\x00\x09\x00\x00\x06', b'\x41\x00\x00\x00\x09\x00\x00\x06']
    for Button_8_Press in Button_8_values:
        if stop_event.is_set():
            break
        ser.write(Button_8_Press)
        print(f"Sent: {Button_8_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_8_Press_Response = ser.read()
        if len(Button_8_Press_Response) > 0:
            print(f"Response: {Button_8_Press_Response.hex()}")
        else:
            print("No response received")

button_8_thread = None

def start_Button_8_thread():
    global button_8_thread
    if not button_8_thread or not button_8_thread.is_alive():
        button_8_thread = threading.Thread(target=Button_8_thread)
        button_8_thread.start()

def stop_Button_8_thread():
    if button_8_thread and button_8_thread.is_alive():
        stop_event.set()
        button_8_thread.join()

## Button 9
def Button_9_thread():
    Button_9_values = [b'\x41\x00\x01\x00\x0a\x00\x00\x06', b'\x41\x00\x00\x00\x0a\x00\x00\x06']
    for Button_9_Press in Button_9_values:
        if stop_event.is_set():
            break
        ser.write(Button_9_Press)
        print(f"Sent: {Button_9_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_9_Press_Response = ser.read()
        if len(Button_9_Press_Response) > 0:
            print(f"Response: {Button_9_Press_Response.hex()}")
        else:
            print("No response received")

button_9_thread = None

def start_Button_9_thread():
    global button_9_thread
    if not button_9_thread or not button_9_thread.is_alive():
        button_9_thread = threading.Thread(target=Button_9_thread)
        button_9_thread.start()

def stop_Button_9_thread():
    if button_9_thread and button_9_thread.is_alive():
        stop_event.set()
        button_9_thread.join()

## Button *
def Button_Pound_thread():
    Button_Pound_values = [b'\x41\x00\x01\x00\x0b\x00\x00\x06', b'\x41\x00\x00\x00\x0b\x00\x00\x06']
    for Button_Pound_Press in Button_Pound_values:
        if stop_event.is_set():
            break
        ser.write(Button_Pound_Press)
        print(f"Sent: {Button_Pound_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_Pound_Press_Response = ser.read()
        if len(Button_Pound_Press_Response) > 0:
            print(f"Response: {Button_Pound_Press_Response.hex()}")
        else:
            print("No response received")

button_Pound_thread = None

def start_Button_Pound_thread():
    global button_Pound_thread
    if not button_Pound_thread or not button_Pound_thread.is_alive():
        button_Pound_thread = threading.Thread(target=Button_Pound_thread)
        button_Pound_thread.start()

def stop_Button_Pound_thread():
    if button_Pound_thread and button_Pound_thread.is_alive():
        stop_event.set()
        button_Pound_thread.join()

## Button #
def Button_Hash_thread():
    Button_Hash_values = [b'\x41\x00\x01\x00\x0c\x00\x00\x06', b'\x41\x00\x00\x00\x0c\x00\x00\x06']
    for Button_Hash_Press in Button_Hash_values:
        if stop_event.is_set():
            break
        ser.write(Button_Hash_Press)
        print(f"Sent: {Button_Hash_Press.hex()}")
        
        # Button Push delay        
        #time.sleep(.1)
                
        # Read the response
        Button_Hash_Press_Response = ser.read()
        if len(Button_Hash_Press_Response) > 0:
            print(f"Response: {Button_Hash_Press_Response.hex()}")
        else:
            print("No response received")

button_Hash_thread = None

def start_Button_Hash_thread():
    global button_Hash_thread
    if not button_Hash_thread or not button_Hash_thread.is_alive():
        button_Hash_thread = threading.Thread(target=Button_Hash_thread)
        button_Hash_thread.start()

def stop_Button_Hash_thread():
    if button_Hash_thread and button_Hash_thread.is_alive():
        stop_event.set()
        button_Hash_thread.join()

## Button Subptt A/B
def Button_SubAB_thread():
    Button_SubAB_values = [b'\x41\x00\x01\x00\x0d\x00\x00\x06', b'\x41\x00\x00\x00\x0d\x00\x00\x06']
    for Button_SubAB_Press in Button_SubAB_values:
        if stop_event.is_set():
            break
        ser.write(Button_SubAB_Press)
        print(f"Sent: {Button_SubAB_Press.hex()}")

        # Button Push delay        
        time.sleep(.1)
                        
        # Read the response
        Button_SubAB_Press_Response = ser.read()
        if len(Button_SubAB_Press_Response) > 0:
            print(f"Response: {Button_SubAB_Press_Response.hex()}")
        else:
            print("No response received")

button_SubAB_thread = None

def start_Button_SubAB_thread():
    global button_SubAB_thread
    if not button_SubAB_thread or not button_SubAB_thread.is_alive():
        button_SubAB_thread = threading.Thread(target=Button_SubAB_thread)
        button_SubAB_thread.start()

def stop_Button_SubAB_thread():
    if button_SubAB_thread and button_SubAB_thread.is_alive():
        stop_event.set()
        button_SubAB_thread.join()

## Button A
def Button_A_thread():
    Button_A_values = [b'\x41\x00\x01\x00\x1a\x00\x00\x06', b'\x41\x00\x00\x00\x1a\x00\x00\x06']
    for Button_A_Press in Button_A_values:
        if stop_event.is_set():
            break
        ser.write(Button_A_Press)
        print(f"Sent: {Button_A_Press.hex()}")

        # Button Push delay        
        time.sleep(.1)

        # Read the response
        Button_A_Press_Response = ser.read()
        if len(Button_A_Press_Response) > 0:
            print(f"Response: {Button_A_Press_Response.hex()}")
        else:
            print("No response received")

    # if Button_A_stop_event.is_set():
    #      pass

button_A_thread = None

def start_Button_A_thread():
    global button_A_thread
    if not button_A_thread or not button_A_thread.is_alive():
        button_A_thread = threading.Thread(target=Button_A_thread)
        button_A_thread.start()

def stop_Button_A_thread():
    if button_A_thread and button_A_thread.is_alive():
        stop_event.set()
        button_A_thread.join()

## Button A Long
def Button_A_Long_thread():
    Button_A_Long_values = [b'\x41\x00\x01\x00\x1a\x00\x00\x06', b'\x41\x00\x01\x01\x1a\x00\x00\x06', b'\x41\x00\x00\x00\x1a\x00\x00\x06']
    for Button_A_Long_Press in Button_A_Long_values:
        if stop_event.is_set():
            break
        ser.write(Button_A_Long_Press)
        print(f"Sent: {Button_A_Long_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_A_Long_Press_Response = ser.read()
        if len(Button_A_Long_Press_Response) > 0:
            print(f"Response: {Button_A_Long_Press_Response.hex()}")
        else:
            print("No response received")

button_A_Long_thread = None

def start_Button_A_Long_thread():
    global button_A_Long_thread
    if not button_A_Long_thread or not button_A_Long_thread.is_alive():
        button_A_Long_thread = threading.Thread(target=Button_A_Long_thread)
        button_A_Long_thread.start()

def stop_Button_A_Long_thread():
    if button_A_Long_thread and button_A_Long_thread.is_alive():
        stop_event.set()
        button_A_Long_thread.join()

## Button B
def Button_B_thread():
    Button_B_values = [b'\x41\x00\x01\x00\x1b\x00\x00\x06', b'\x41\x00\x00\x00\x1b\x00\x00\x06']
    for Button_B_Press in Button_B_values:
        if stop_event.is_set():
            break
        ser.write(Button_B_Press)
        print(f"Sent: {Button_B_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_B_Press_Response = ser.read()
        if len(Button_B_Press_Response) > 0:
            print(f"Response: {Button_B_Press_Response.hex()}")
        else:
            print("No response received")

button_B_thread = None

def start_Button_B_thread():
    global button_B_thread
    if not button_B_thread or not button_B_thread.is_alive():
        button_B_thread = threading.Thread(target=Button_B_thread)
        button_B_thread.start()

def stop_Button_B_thread():
    if button_B_thread and button_B_thread.is_alive():
        stop_event.set()
        button_B_thread.join()

## Button B Long
def Button_B_Long_thread():
    Button_B_Long_values = [b'\x41\x00\x01\x00\x1b\x00\x00\x06', b'\x41\x00\x01\x01\x1b\x00\x00\x06', b'\x41\x00\x00\x00\x1b\x00\x00\x06']
    for Button_B_Long_Press in Button_B_Long_values:
        if stop_event.is_set():
            break
        ser.write(Button_B_Long_Press)
        print(f"Sent: {Button_B_Long_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_B_Long_Press_Response = ser.read()
        if len(Button_B_Long_Press_Response) > 0:
            print(f"Response: {Button_B_Long_Press_Response.hex()}")
        else:
            print("No response received")

button_B_Long_thread = None

def start_Button_B_Long_thread():
    global button_B_Long_thread
    if not button_B_Long_thread or not button_B_Long_thread.is_alive():
        button_B_Long_thread = threading.Thread(target=Button_B_Long_thread)
        button_B_Long_thread.start()

def stop_Button_B_Long_thread():
    if button_B_Long_thread and button_B_Long_thread.is_alive():
        stop_event.set()
        button_B_Long_thread.join()

## Button C
def Button_C_thread():
    Button_C_values = [b'\x41\x00\x01\x00\x1c\x00\x00\x06', b'\x41\x00\x00\x00\x1c\x00\x00\x06']
    for Button_C_Press in Button_C_values:
        if stop_event.is_set():
            break
        ser.write(Button_C_Press)
        print(f"Sent: {Button_C_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_C_Press_Response = ser.read()
        if len(Button_C_Press_Response) > 0:
            print(f"Response: {Button_C_Press_Response.hex()}")
        else:
            print("No response received")

button_C_thread = None

def start_Button_C_thread():
    global button_C_thread
    if not button_C_thread or not button_C_thread.is_alive():
        button_C_thread = threading.Thread(target=Button_C_thread)
        button_C_thread.start()

def stop_Button_C_thread():
    if button_C_thread and button_C_thread.is_alive():
        stop_event.set()
        button_C_thread.join()

## Button C Long
def Button_C_Long_thread():
    Button_C_Long_values = [b'\x41\x00\x01\x00\x1c\x00\x00\x06', b'\x41\x00\x01\x01\x1c\x00\x00\x06', b'\x41\x00\x00\x00\x1c\x00\x00\x06']
    for Button_C_Long_Press in Button_C_Long_values:
        if stop_event.is_set():
            break
        ser.write(Button_C_Long_Press)
        print(f"Sent: {Button_C_Long_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_C_Long_Press_Response = ser.read()
        if len(Button_C_Long_Press_Response) > 0:
            print(f"Response: {Button_C_Long_Press_Response.hex()}")
        else:
            print("No response received")

button_C_Long_thread = None

def start_Button_C_Long_thread():
    global button_C_Long_thread
    if not button_C_Long_thread or not button_C_Long_thread.is_alive():
        button_C_Long_thread = threading.Thread(target=Button_C_Long_thread)
        button_C_Long_thread.start()

def stop_Button_C_Long_thread():
    if button_C_Long_thread and button_C_Long_thread.is_alive():
        stop_event.set()
        button_C_Long_thread.join()

## Button D
def Button_D_thread():
    Button_D_values = [b'\x41\x00\x01\x00\x1d\x00\x00\x06', b'\x41\x00\x00\x00\x1d\x00\x00\x06']
    for Button_D_Press in Button_D_values:
        if stop_event.is_set():
            break
        ser.write(Button_D_Press)
        print(f"Sent: {Button_D_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.05)
                
        # Read the response
        Button_D_Press_Response = ser.read()
        if len(Button_D_Press_Response) > 0:
            print(f"Response: {Button_D_Press_Response.hex()}")
        else:
            print("No response received")

button_D_thread = None

def start_Button_D_thread():
    global button_D_thread
    if not button_D_thread or not button_D_thread.is_alive():
        button_D_thread = threading.Thread(target=Button_D_thread)
        button_D_thread.start()

def stop_Button_D_thread():
    if button_D_thread and button_D_thread.is_alive():
        stop_event.set()
        button_D_thread.join()

## Button D Long
def Button_D_Long_thread():
    Button_D_Long_values = [b'\x41\x00\x01\x00\x1d\x00\x00\x06', b'\x41\x00\x01\x01\x1d\x00\x00\x06', b'\x41\x00\x00\x00\x1d\x00\x00\x06']
    for Button_D_Long_Press in Button_D_Long_values:
        if stop_event.is_set():
            break
        ser.write(Button_D_Long_Press)
        print(f"Sent: {Button_D_Long_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_D_Long_Press_Response = ser.read()
        if len(Button_D_Long_Press_Response) > 0:
            print(f"Response: {Button_D_Long_Press_Response.hex()}")
        else:
            print("No response received")

button_D_Long_thread = None

def start_Button_D_Long_thread():
    global button_D_Long_thread
    if not button_D_Long_thread or not button_D_Long_thread.is_alive():
        button_D_Long_thread = threading.Thread(target=Button_D_Long_thread)
        button_D_Long_thread.start()

def stop_Button_D_Long_thread():
    if button_D_Long_thread and button_D_Long_thread.is_alive():
        stop_event.set()
        button_D_Long_thread.join()

## Button UP
def Button_UP_thread():
    Button_UP_values = [b'\x41\x00\x01\x00\x10\x00\x00\x06', b'\x41\x00\x00\x00\x10\x00\x00\x06']
    for Button_UP_Press in Button_UP_values:
        if stop_event.is_set():
            break
        ser.write(Button_UP_Press)
        print(f"Sent: {Button_UP_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_UP_Press_Response = ser.read()
        if len(Button_UP_Press_Response) > 0:
            print(f"Response: {Button_UP_Press_Response.hex()}")
        else:
            print("No response received")

button_UP_thread = None

def start_Button_UP_thread():
    global button_UP_thread
    if not button_UP_thread or not button_UP_thread.is_alive():
        button_UP_thread = threading.Thread(target=Button_UP_thread)
        button_UP_thread.start()

def stop_Button_UP_thread():
    if button_UP_thread and button_UP_thread.is_alive():
        stop_event.set()
        button_UP_thread.join()

## Button DOWN
def Button_DOWN_thread():
    Button_DOWN_values = [b'\x41\x00\x01\x00\x11\x00\x00\x06', b'\x41\x00\x00\x00\x11\x00\x00\x06']
    for Button_DOWN_Press in Button_DOWN_values:
        if stop_event.is_set():
            break
        ser.write(Button_DOWN_Press)
        print(f"Sent: {Button_DOWN_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_DOWN_Press_Response = ser.read()
        if len(Button_DOWN_Press_Response) > 0:
            print(f"Response: {Button_DOWN_Press_Response.hex()}")
        else:
            print("No response received")

button_DOWN_thread = None

def start_Button_DOWN_thread():
    global button_DOWN_thread
    if not button_DOWN_thread or not button_DOWN_thread.is_alive():
        button_DOWN_thread = threading.Thread(target=Button_DOWN_thread)
        button_DOWN_thread.start()

def stop_Button_DOWN_thread():
    if button_DOWN_thread and button_DOWN_thread.is_alive():
        stop_event.set()
        button_DOWN_thread.join()

##########################

# Handmic up/down buttons
button_up = tk.Button(window, text="UP", font=("Arial Black", 10, "bold"), foreground="white", background="#262626", highlightthickness=0, border=0, padx=14, pady=-20, command=start_Button_UP_thread)
button_up.place(x=211,y=18)
button_down = tk.Button(window, text="DN", font=("Arial Black", 10, "bold"), foreground="white", background="#262626", highlightthickness=0, border=0, padx=14, pady=-20, command=start_Button_DOWN_thread)
button_down.place(x=134,y=18)

# Number pad
button_1_x = 149
button_1_y = 132
button_1 = tk.Button(window, text="1", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_1_thread)
button_1.place(x=button_1_x,y=button_1_y)
button_1_label = tk.Label(window, text=" !  < ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_1_label.place(x=button_1_x,y=button_1_y+25)

button_2 = tk.Button(window, text="2", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_2_thread)
button_2.place(x=button_1_x+(68*1),y=button_1_y)
button_2_label = tk.Label(window, text="ABC", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_2_label.place(x=button_1_x+(68*1),y=button_1_y+25)

button_3 = tk.Button(window, text="3", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_3_thread)
button_3.place(x=button_1_x+(68*2),y=button_1_y)
button_3_label = tk.Label(window, text="DEF ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_3_label.place(x=button_1_x+(68*2),y=button_1_y+25)

button_4 = tk.Button(window, text="4", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_4_thread)
button_4.place(x=button_1_x+(68*0),y=button_1_y+(50*1))
button_4_label = tk.Label(window, text="GHI ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_4_label.place(x=button_1_x+(68*0),y=button_1_y+(25*3))

button_5 = tk.Button(window, text="5", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_5_thread)
button_5.place(x=button_1_x+(68*1),y=button_1_y+(50*1))
button_5_label = tk.Label(window, text="JKL ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_5_label.place(x=button_1_x+(68*1),y=button_1_y+(25*3))

button_6 = tk.Button(window, text="6", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_6_thread)
button_6.place(x=button_1_x+(68*2),y=button_1_y+(50*1))
button_6_label = tk.Label(window, text="MNO", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_6_label.place(x=button_1_x+(68*2),y=button_1_y+(25*3))

button_7 = tk.Button(window, text="7", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_7_thread)
button_7.place(x=button_1_x+(68*0),y=button_1_y+(50*2))
button_7_label = tk.Label(window, text="PQRS ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=0, pady=-20)
button_7_label.place(x=button_1_x+(68*0),y=button_1_y+(25*5))

button_8 = tk.Button(window, text="8", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_8_thread)
button_8.place(x=button_1_x+(68*1),y=button_1_y+(50*2))
button_8_label = tk.Label(window, text="TUV", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_8_label.place(x=button_1_x+(68*1),y=button_1_y+(25*5))

button_9 = tk.Button(window, text="9", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_9_thread)
button_9.place(x=button_1_x+(68*2),y=button_1_y+(50*2))
button_9_label = tk.Label(window, text="WXYZ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=0, pady=-20)
button_9_label.place(x=button_1_x+(68*2),y=button_1_y+(25*5))

button_pound = tk.Button(window, text="*", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_Pound_thread)
button_pound.place(x=button_1_x+(68*0),y=button_1_y+(50*3))
button_pound_label = tk.Label(window, text="[___]", font=("Arial Black", 7, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=.5)
button_pound_label.place(x=button_1_x+(68*0),y=button_1_y+(25*7))

button_0 = tk.Button(window, text="0", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_0_thread)
button_0.place(x=button_1_x+(68*1),y=button_1_y+(50*3))
button_0_label = tk.Label(window, text="+", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=15, pady=-20)
button_0_label.place(x=button_1_x+(68*1),y=button_1_y+(25*7))

button_hash = tk.Button(window, text="#", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20, command=start_Button_Hash_thread)
button_hash.place(x=button_1_x+(68*2),y=button_1_y+(50*3))
button_hash_label = tk.Label(window, text="⇧", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=14, pady=-20)
button_hash_label.place(x=button_1_x+(68*2),y=button_1_y+(25*7))

# # A thru D buttons
button_size = 60
button_A_x = 102
button_A_y = 340

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "button_A.png")
buton_A_image = Image.open(image_path)
resize_button_A = buton_A_image.resize((button_size, button_size), Image.ANTIALIAS)
button_A = ImageTk.PhotoImage(resize_button_A)
button_A_button = tk.Button(window, image=button_A, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0, height=button_size-8, width=button_size-8, command=start_Button_A_thread)
button_A_button.place(x=button_A_x,y=button_A_y)

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "button_B.png")
buton_B_image = Image.open(image_path)
resize_button_B = buton_B_image.resize((button_size, button_size), Image.ANTIALIAS)
button_B = ImageTk.PhotoImage(resize_button_B)
button_B_button = tk.Button(window, image=button_B, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0, height=button_size-8, width=button_size-8, command=start_Button_B_thread)
button_B_button.place(x=button_A_x+(58*1),y=button_A_y)
                          
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "button_C.png")
buton_C_image = Image.open(image_path)
resize_button_C = buton_C_image.resize((button_size, button_size), Image.ANTIALIAS)
button_C = ImageTk.PhotoImage(resize_button_C)
button_C_button = tk.Button(window, image=button_C, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0, height=button_size-8, width=button_size-8, command=start_Button_C_thread)
button_C_button.place(x=button_A_x+(58*2),y=button_A_y)

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "button_D.png")
buton_D_image = Image.open(image_path)
resize_button_D = buton_D_image.resize((button_size, button_size), Image.ANTIALIAS)
button_D = ImageTk.PhotoImage(resize_button_D)
button_D_button = tk.Button(window, image=button_D, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0, height=button_size-8, width=button_size-8, command=start_Button_D_thread)
button_D_button.place(x=button_A_x+(58*3),y=button_A_y)

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "subptt.png")
button_subptt_image = Image.open(image_path)
resize_subptt = button_subptt_image.resize((40, 101), Image.ANTIALIAS)
button_subptt = ImageTk.PhotoImage(resize_subptt)
button_subptt_button = tk.Button(window, image=button_subptt, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0, command=start_Button_SubAB_thread)
button_subptt_button.place(x=74,y=141)

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "button_ptt.png")
button_ptt_image = Image.open(image_path)
resize_button_ptt = button_ptt_image.resize((71, 59), Image.ANTIALIAS)
button_ptt = ImageTk.PhotoImage(resize_button_ptt)
button_ptt_button = PTTButton(window, image=button_ptt, border=0, highlightthickness=0, padx=0, pady=0)
button_ptt_button.place(x=20, y=20)
#button_ptt_label = tk.Label(window, text="PTT", font=("Arial Black", 10, "bold"), anchor="s", foreground="white", border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B")
#button_ptt_label.place(x=40, y=40)
red_light = tk.Label(window, bg="#F0F0F0", width=1, height=1, bd=0, highlightthickness=1, highlightbackground="gray", relief="solid")
red_light.place(x=30, y=30)

# Define the thread function for serial communication
def serial_thread():
    # Check if the port is open
    if ser.is_open:
        print(f"Connected to {port}")
        red_light.configure(bg="#00C800") #Green

        while not ser_stop_event.is_set():
            if stop_event.is_set():
                break
            # Send the hex value
            IRP_MJ_WRITE = b'\x06'
            ser.write(IRP_MJ_WRITE)
#            print(f"IRP_MJ_WRITE: {IRP_MJ_WRITE.hex()}")

            # Read the response
            IRP_MJ_READ = ser.read()
            if len(IRP_MJ_READ) > 0:
#                print(f"IRP_MJ_READ: {IRP_MJ_READ.hex()}")
                pass
            else:
#                print("No response received")
                pass

            # Wait for 1 second
            time.sleep(1)

        # Close the serial port
        #red_light.configure(bg="#F0F0F0") #Gray
        ser.close()
        print("Serial port closed")
        pass
    else:
        print(f"Failed to connect to {port}")

# Create and start the serial thread
serial_thread = threading.Thread(target=serial_thread)
serial_thread.start()

def close_window():
    stop_event.set()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", close_window)

window.mainloop()

# Wait for the serial thread to complete
serial_thread.join()