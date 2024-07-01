import tkinter as tk
import pyqrcode
from tkinter import messagebox

def generate_qr():
    url = url_entry.get()
    if url:
        qr_code = pyqrcode.create(url)
        qr_code.svg('qrcode.svg', scale=5)
        messagebox.showinfo("Success", "QR Code generated successfully!")
    else:
        messagebox.showerror("Error", "Please enter a URL.")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create a label and an entry for URL input
url_label = tk.Label(root, text="Enter URL to generate QR code:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create a button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()