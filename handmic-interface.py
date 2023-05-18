import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import os

callsign = "KI5QPY"

for file in os.listdir('./at-d578uvIII-handmic'):
    print(file)

# GUI Window
window = tk.Tk()
window.title("Handmic Emulator - Anytone AT-D578UVIII")
window.geometry("400x600")
window.resizable(False,False)

# Mic Image
image = Image.open("at-d578uvIII-handmic/AT-D578UVIII.png")
resized_image = image.resize((303, 578), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(resized_image)
background_label = tk.Label(window, image=tk_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Callsign overlay
label = tk.Label(window, text=callsign, font=("Arial", 19, "bold italic"), foreground="white", background="#262626", padx=0, pady=0)
label.place(x=155,y=72)

# Handmic button_s
button_up = tk.Button(window, text="UP", font=("Arial Black", 10, "bold"), foreground="white", background="#262626", highlightthickness=0, border=0, padx=14, pady=-20)
button_up.place(x=211,y=18)
button_down = tk.Button(window, text="DN", font=("Arial Black", 10, "bold"), foreground="white", background="#262626", highlightthickness=0, border=0, padx=14, pady=-20)
button_down.place(x=134,y=18)

# Number pad
button_1_x = 149
button_1_y = 132
button_1 = tk.Button(window, text="1", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_1.place(x=button_1_x,y=button_1_y)
button_1_label = tk.Label(window, text=" !  < ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_1_label.place(x=button_1_x,y=button_1_y+25)

button_2 = tk.Button(window, text="2", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_2.place(x=button_1_x+(68*1),y=button_1_y)
button_2_label = tk.Label(window, text="ABC", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_2_label.place(x=button_1_x+(68*1),y=button_1_y+25)

button_3 = tk.Button(window, text="3", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_3.place(x=button_1_x+(68*2),y=button_1_y)
button_3_label = tk.Label(window, text="DEF ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_3_label.place(x=button_1_x+(68*2),y=button_1_y+25)

button_4 = tk.Button(window, text="4", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_4.place(x=button_1_x+(68*0),y=button_1_y+(50*1))
button_4_label = tk.Label(window, text="GHI ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_4_label.place(x=button_1_x+(68*0),y=button_1_y+(25*3))

button_5 = tk.Button(window, text="5", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_5.place(x=button_1_x+(68*1),y=button_1_y+(50*1))
button_5_label = tk.Label(window, text="JKL ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_5_label.place(x=button_1_x+(68*1),y=button_1_y+(25*3))

button_6 = tk.Button(window, text="6", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_6.place(x=button_1_x+(68*2),y=button_1_y+(50*1))
button_6_label = tk.Label(window, text="MNO", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_6_label.place(x=button_1_x+(68*2),y=button_1_y+(25*3))

button_7 = tk.Button(window, text="7", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_7.place(x=button_1_x+(68*0),y=button_1_y+(50*2))
button_7_label = tk.Label(window, text="PQRS ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=0, pady=-20)
button_7_label.place(x=button_1_x+(68*0),y=button_1_y+(25*5))

button_8 = tk.Button(window, text="8", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_8.place(x=button_1_x+(68*1),y=button_1_y+(50*2))
button_8_label = tk.Label(window, text="TUV", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_8_label.place(x=button_1_x+(68*1),y=button_1_y+(25*5))

button_9 = tk.Button(window, text="9", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_9.place(x=button_1_x+(68*2),y=button_1_y+(50*2))
button_9_label = tk.Label(window, text="WXYZ", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=0, pady=-20)
button_9_label.place(x=button_1_x+(68*2),y=button_1_y+(25*5))

button_pound = tk.Button(window, text="*", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_pound.place(x=button_1_x+(68*0),y=button_1_y+(50*3))
button_pound_label = tk.Label(window, text="[___]", font=("Arial Black", 7, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=.5)
button_pound_label.place(x=button_1_x+(68*0),y=button_1_y+(25*7))

button_0 = tk.Button(window, text="0", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_0.place(x=button_1_x+(68*1),y=button_1_y+(50*3))
button_0_label = tk.Label(window, text="+", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=15, pady=-20)
button_0_label.place(x=button_1_x+(68*1),y=button_1_y+(25*7))

button_hash = tk.Button(window, text="#", font=("Arial Black", 14, "bold"), anchor="n", foreground="white", background="#262626", highlightthickness=0, border=0, padx=6, pady=-20)
button_hash.place(x=button_1_x+(68*2),y=button_1_y+(50*3))
button_hash_label = tk.Label(window, text="⇧", font=("Arial Black", 8, "bold"), anchor="s", foreground="white", background="#262626", highlightthickness=0, border=0, padx=14, pady=-20)
button_hash_label.place(x=button_1_x+(68*2),y=button_1_y+(25*7))

# # A thru D buttons
button_size = 60
button_A_x = 102
button_A_y = 340

buton_A_image = Image.open("./at-d578uvIII-handmic/button_A.png")
resize_button_A = buton_A_image.resize((button_size, button_size), Image.ANTIALIAS)
button_A = ImageTk.PhotoImage(resize_button_A)
button_A_button = tk.Button(window, image=button_A, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0, height=button_size-8, width=button_size-8)
button_A_button.place(x=button_A_x,y=button_A_y)

buton_B_image = Image.open("./at-d578uvIII-handmic/button_B.png")
resize_button_B = buton_B_image.resize((button_size, button_size), Image.ANTIALIAS)
button_B = ImageTk.PhotoImage(resize_button_B)
button_B_button = tk.Button(window, image=button_B, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0, height=button_size-8, width=button_size-8)
button_B_button.place(x=button_A_x+(58*1),y=button_A_y)
                          
buton_C_image = Image.open("./at-d578uvIII-handmic/button_C.png")
resize_button_C = buton_C_image.resize((button_size, button_size), Image.ANTIALIAS)
button_C = ImageTk.PhotoImage(resize_button_C)
button_C_button = tk.Button(window, image=button_C, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0, height=button_size-8, width=button_size-8)
button_C_button.place(x=button_A_x+(58*2),y=button_A_y)

buton_D_image = Image.open("./at-d578uvIII-handmic/button_D.png")
resize_button_D = buton_D_image.resize((button_size, button_size), Image.ANTIALIAS)
button_D = ImageTk.PhotoImage(resize_button_D)
button_D_button = tk.Button(window, image=button_D, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0, height=button_size-8, width=button_size-8)
button_D_button.place(x=button_A_x+(58*3),y=button_A_y)

button_subptt_image = Image.open("./at-d578uvIII-handmic/subptt.png")
resize_subptt = button_subptt_image.resize((40, 101), Image.ANTIALIAS)
button_subptt = ImageTk.PhotoImage(resize_subptt)
button_subptt_button = tk.Button(window, image=button_subptt, border=0, highlightthickness=0, background="#2B2B2B", activebackground="#2B2B2B", padx=0, pady=0)
button_subptt_button.place(x=74,y=141)


window.mainloop()