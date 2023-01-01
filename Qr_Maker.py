import pyqrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Ask for Input
my_inp = str(input("Enter Your Link : "))

# Create the QR code
qr = pyqrcode.create(my_inp)

# Save the QR code as a PNG file
qr.png('qr_code.png', scale=8)

# Load the QR code image
image = Image.open('qr_code.png')

# Create the GUI window
window = tk.Tk()
window.title('QR Code')

# Add the image to the GUI window
image_tk = ImageTk.PhotoImage(image)
label = tk.Label(window, image=image_tk)
label.pack()

# Run the GUI loop
window.mainloop()
