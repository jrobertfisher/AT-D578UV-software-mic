#
#Ideas and references to look into:
#   Program Mode: \x50\x52\x4f\x47\x52\x41\x4d and response: \x51\x58\x06
#   Read Device ID: \x02 more - https://github.com/reald/anytone-flash-tools/blob/master/at-d878uv_protocol.md
#   End: \x45\x4e\x44 and response: \x06

import serial
import time
import threading

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

# Define the thread function for serial communication
def serial_thread():
    # Check if the port is open
    if ser.is_open:
        print(f"Connected to {port}")

        while not stop_event.is_set():
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
        ser.close()
        print("Serial port closed")
    else:
        print(f"Failed to connect to {port}")

# Create and start the serial thread
serial_thread = threading.Thread(target=serial_thread)
serial_thread.start()

def Button_PTT():
    Button_PTT_values = [b'\x41\x01\x00\x00\x00\x00\x00\x06', b'\x41\x00\x00\x00\x00\x00\x00\x06']
    for Button_PTT_Press in Button_PTT_values:
        ser.write(Button_PTT_Press)
        print(f"Sent: {Button_PTT_Press.hex()}")

        # Button Push delay        
        time.sleep(1)
                        
        # Read the response
        Button_PTT_Press_Response = ser.read()
        if len(Button_PTT_Press_Response) > 0:
            print(f"Response: {Button_PTT_Press_Response.hex()}")
        else:
            print("No response received")

def Button_0():
    Button_0_values = [b'\x41\x00\x01\x00\x01\x00\x00\x06', b'\x41\x00\x00\x00\x01\x00\x00\x06']
    for Button_0_Press in Button_0_values:
        ser.write(Button_0_Press)
        print(f"Sent: {Button_0_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_0_Press_Response = ser.read()
        if len(Button_0_Press_Response) > 0:
            print(f"Response: {Button_0_Press_Response.hex()}")
        else:
            print("No response received")

def Button_1():
    Button_1_values = [b'\x41\x00\x01\x00\x02\x00\x00\x06', b'\x41\x00\x00\x00\x02\x00\x00\x06']
    for Button_1_Press in Button_1_values:
        ser.write(Button_1_Press)
        print(f"Sent: {Button_1_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_1_Press_Response = ser.read()
        if len(Button_1_Press_Response) > 0:
            print(f"Response: {Button_1_Press_Response.hex()}")
        else:
            print("No response received")

def Button_2():
    Button_2_values = [b'\x41\x00\x01\x00\x03\x00\x00\x06', b'\x41\x00\x00\x00\x03\x00\x00\x06']
    for Button_2_Press in Button_2_values:
        ser.write(Button_2_Press)
        print(f"Sent: {Button_2_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_2_Press_Response = ser.read()
        if len(Button_2_Press_Response) > 0:
            print(f"Response: {Button_2_Press_Response.hex()}")
        else:
            print("No response received")

def Button_3():
    Button_3_values = [b'\x41\x00\x01\x00\x04\x00\x00\x06', b'\x41\x00\x00\x00\x04\x00\x00\x06']
    for Button_3_Press in Button_3_values:
        ser.write(Button_3_Press)
        print(f"Sent: {Button_3_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_3_Press_Response = ser.read()
        if len(Button_3_Press_Response) > 0:
            print(f"Response: {Button_3_Press_Response.hex()}")
        else:
            print("No response received")

def Button_4():
    Button_4_values = [b'\x41\x00\x01\x00\x05\x00\x00\x06', b'\x41\x00\x00\x00\x05\x00\x00\x06']
    for Button_4_Press in Button_4_values:
        ser.write(Button_4_Press)
        print(f"Sent: {Button_4_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_4_Press_Response = ser.read()
        if len(Button_4_Press_Response) > 0:
            print(f"Response: {Button_4_Press_Response.hex()}")
        else:
            print("No response received")

def Button_5():
    Button_5_values = [b'\x41\x00\x01\x00\x06\x00\x00\x06', b'\x41\x00\x00\x00\x06\x00\x00\x06']
    for Button_5_Press in Button_5_values:
        ser.write(Button_5_Press)
        print(f"Sent: {Button_5_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_5_Press_Response = ser.read()
        if len(Button_5_Press_Response) > 0:
            print(f"Response: {Button_5_Press_Response.hex()}")
        else:
            print("No response received")

def Button_6():
    Button_6_values = [b'\x41\x00\x01\x00\x07\x00\x00\x06', b'\x41\x00\x00\x00\x07\x00\x00\x06']
    for Button_6_Press in Button_6_values:
        ser.write(Button_6_Press)
        print(f"Sent: {Button_6_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_6_Press_Response = ser.read()
        if len(Button_6_Press_Response) > 0:
            print(f"Response: {Button_6_Press_Response.hex()}")
        else:
            print("No response received")

def Button_7():
    Button_7_values = [b'\x41\x00\x01\x00\x08\x00\x00\x06', b'\x41\x00\x00\x00\x08\x00\x00\x06']
    for Button_7_Press in Button_7_values:
        ser.write(Button_7_Press)
        print(f"Sent: {Button_7_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_7_Press_Response = ser.read()
        if len(Button_7_Press_Response) > 0:
            print(f"Response: {Button_7_Press_Response.hex()}")
        else:
            print("No response received")

def Button_8():
    Button_8_values = [b'\x41\x00\x01\x00\x09\x00\x00\x06', b'\x41\x00\x00\x00\x09\x00\x00\x06']
    for Button_8_Press in Button_8_values:
        ser.write(Button_8_Press)
        print(f"Sent: {Button_8_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_8_Press_Response = ser.read()
        if len(Button_8_Press_Response) > 0:
            print(f"Response: {Button_8_Press_Response.hex()}")
        else:
            print("No response received")

def Button_9():
    Button_9_values = [b'\x41\x00\x01\x00\x0a\x00\x00\x06', b'\x41\x00\x00\x00\x0a\x00\x00\x06']
    for Button_9_Press in Button_9_values:
        ser.write(Button_9_Press)
        print(f"Sent: {Button_9_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_9_Press_Response = ser.read()
        if len(Button_9_Press_Response) > 0:
            print(f"Response: {Button_9_Press_Response.hex()}")
        else:
            print("No response received")

def Button_Pound():
    Button_Pound_values = [b'\x41\x00\x01\x00\x0b\x00\x00\x06', b'\x41\x00\x00\x00\x0b\x00\x00\x06']
    for Button_Pound_Press in Button_Pound_values:
        ser.write(Button_Pound_Press)
        print(f"Sent: {Button_Pound_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_Pound_Press_Response = ser.read()
        if len(Button_Pound_Press_Response) > 0:
            print(f"Response: {Button_Pound_Press_Response.hex()}")
        else:
            print("No response received")

def Button_Hash():
    Button_Hash_values = [b'\x41\x00\x01\x00\x0c\x00\x00\x06', b'\x41\x00\x00\x00\x0c\x00\x00\x06']
    for Button_Hash_Press in Button_Hash_values:
        ser.write(Button_Hash_Press)
        print(f"Sent: {Button_Hash_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_Hash_Press_Response = ser.read()
        if len(Button_Hash_Press_Response) > 0:
            print(f"Response: {Button_Hash_Press_Response.hex()}")
        else:
            print("No response received")

def Button_SubAB():
    Button_SubAB_values = [b'\x41\x00\x01\x00\x0d\x00\x00\x06', b'\x41\x00\x00\x00\x0d\x00\x00\x06']
    for Button_SubAB_Press in Button_SubAB_values:
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

def Button_A():
    Button_A_values = [b'\x41\x00\x01\x00\x1a\x00\x00\x06', b'\x41\x00\x00\x00\x1a\x00\x00\x06']
    for Button_A_Press in Button_A_values:
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

def Button_A_Long():
    Button_A_Long_values = [b'\x41\x00\x01\x00\x1a\x00\x00\x06', b'\x41\x00\x01\x01\x1a\x00\x00\x06', b'\x41\x00\x00\x00\x1a\x00\x00\x06']
    for Button_A_Long_Press in Button_A_Long_values:
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

def Button_B():
    Button_B_values = [b'\x41\x00\x01\x00\x1b\x00\x00\x06', b'\x41\x00\x00\x00\x1b\x00\x00\x06']
    for Button_B_Press in Button_B_values:
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

def Button_B_Long():
    Button_B_Long_values = [b'\x41\x00\x01\x00\x1b\x00\x00\x06', b'\x41\x00\x01\x01\x1b\x00\x00\x06', b'\x41\x00\x00\x00\x1b\x00\x00\x06']
    for Button_B_Long_Press in Button_B_Long_values:
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

def Button_C():
    Button_C_values = [b'\x41\x00\x01\x00\x1c\x00\x00\x06', b'\x41\x00\x00\x00\x1c\x00\x00\x06']
    for Button_C_Press in Button_C_values:
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

def Button_C_Long():
    Button_C_Long_values = [b'\x41\x00\x01\x00\x1c\x00\x00\x06', b'\x41\x00\x01\x01\x1c\x00\x00\x06', b'\x41\x00\x00\x00\x1c\x00\x00\x06']
    for Button_C_Long_Press in Button_C_Long_values:
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

def Button_D():
    Button_D_values = [b'\x41\x00\x01\x00\x1d\x00\x00\x06', b'\x41\x00\x00\x00\x1d\x00\x00\x06']
    for Button_D_Press in Button_D_values:
        ser.write(Button_D_Press)
        print(f"Sent: {Button_D_Press.hex()}")
        
        # Button Push delay        
        time.sleep(.1)
                
        # Read the response
        Button_D_Press_Response = ser.read()
        if len(Button_D_Press_Response) > 0:
            print(f"Response: {Button_D_Press_Response.hex()}")
        else:
            print("No response received")

def Button_D_Long():
    Button_D_Long_values = [b'\x41\x00\x01\x00\x1d\x00\x00\x06', b'\x41\x00\x01\x01\x1d\x00\x00\x06', b'\x41\x00\x00\x00\x1d\x00\x00\x06']
    for Button_D_Long_Press in Button_D_Long_values:
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

def Button_UP():
    Button_UP_values = [b'\x41\x00\x01\x00\x10\x00\x00\x06', b'\x41\x00\x00\x00\x10\x00\x00\x06']
    for Button_UP_Press in Button_UP_values:
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

def Button_DOWN():
    Button_DOWN_values = [b'\x41\x00\x01\x00\x11\x00\x00\x06', b'\x41\x00\x00\x00\x11\x00\x00\x06']
    for Button_DOWN_Press in Button_DOWN_values:
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


# Main thread continues running and prompts for user input
while True:
    print("User Options:")
    print("0. Option 0 ")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Option 6")
    print("7. Option 7")
    print("8. Option 8")
    print("9. Option 9")
    print("*. Option *")
    print("#. Option #")
    print("A. Option A")
    print("B. Option B")
    print("C. Option C")
    print("D. Option D")
    print("+. Option UP")
    print("-. Option DOWN")
    print("PTT. Option PTT")
    print("Exit. Exit")

    user_input = input("Enter an option: ")

    if user_input == '1':
        # Handle Option 1 command
        # Example:
        print("Option 1 selected")
        Button_1()
    elif user_input == '2':
        # Handle Option 2 command
        # Example:
        print("Option 2 selected")
        Button_2()
    elif user_input == '3':
        # Handle Option 3 command
        # Example:
        print("Option 3 selected")
        Button_3()
    elif user_input == '4':
        # Handle Option 4 command
        # Example:
        print("Option 4 selected")
        Button_4()
    elif user_input == '5':
        # Handle Option 5 command
        # Example:
        print("Option 5 selected")
        Button_5()
    elif user_input == '6':
        # Handle Option 6 command
        # Example:
        print("Option 6 selected")
        Button_6()
    elif user_input == '7':
        # Handle Option 7 command
        # Example:
        print("Option 7 selected")
        Button_7()
    elif user_input == '8':
        # Handle Option 8 command
        # Example:
        print("Option 8 selected")
        Button_8()
    elif user_input == '9':
        # Handle Option 9 command
        # Example:
        print("Option 9 selected")
        Button_9()
    elif user_input == '0':
        # Handle Option 0 command
        # Example:
        print("Option 0 selected")
        Button_0()
    elif user_input == '*':
        # Handle Option * command
        # Example:
        print("Option * selected")
        Button_Pound()
    elif user_input == '#':
        # Handle Option # command
        # Example:
        print("Option # selected")
        Button_Hash()
    elif user_input == 'A':
        # Handle Option A command
        # Example:
        print("Option A selected")
        Button_A()
    elif user_input == 'B':
        # Handle Option B command
        # Example:
        print("Option B selected")
        Button_B()
    elif user_input == 'C':
        # Handle Option C command
        # Example:
        print("Option C selected")
        Button_C()
    elif user_input == 'D':
        # Handle Option D command
        # Example:
        print("Option D selected")
        Button_D()
    elif user_input == '+':
        # Handle Option + command
        # Example:
        print("Option + selected")
        Button_UP()
    elif user_input == '-':
        # Handle Option D command
        # Example:
        print("Option - selected")
        Button_DOWN()
    elif user_input == 'PTT':
        # Handle Option PTT command
        # Example:
        print("Option PTT selected")
        Button_PTT()
    elif user_input == 'Exit':
        # Set the stop event to terminate the serial thread
        stop_event.set()
        break
    else:
        print("Invalid option")

# Wait for the serial thread to complete
serial_thread.join()