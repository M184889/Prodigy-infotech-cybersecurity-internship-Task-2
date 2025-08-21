import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import os

def encrypt_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    key = key_entry.get()
    if not key.isdigit() or not (0 <= int(key) <= 255):
        messagebox.showerror("Error", "Key must be a number between 0 and 255")
        return

    key = int(key)
    img = Image.open(file_path)
    img_array = np.array(img)
    encrypted_array = img_array ^ key
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))

    save_path = os.path.splitext(file_path)[0] + "_encrypted.png"
    encrypted_img.save(save_path)
    messagebox.showinfo("Success", f"Image encrypted and saved as {save_path}")

def decrypt_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    key = key_entry.get()
    if not key.isdigit() or not (0 <= int(key) <= 255):
        messagebox.showerror("Error", "Key must be a number between 0 and 255")
        return

    key = int(key)
    img = Image.open(file_path)
    img_array = np.array(img)
    decrypted_array = img_array ^ key
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))

    save_path = os.path.splitext(file_path)[0] + "_decrypted.png"
    decrypted_img.save(save_path)
    messagebox.showinfo("Success", f"Image decrypted and saved as {save_path}")

# GUI Setup
root = tk.Tk()
root.title("Pixel Manipulation - Image Encryption Tool")
root.geometry("400x250")
root.configure(bg="#2c3e50")

title_label = tk.Label(root, text="Image Encryption Tool", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50")
title_label.pack(pady=10)

tk.Label(root, text="Enter Key (0-255):", fg="white", bg="#2c3e50", font=("Arial", 12)).pack(pady=5)
key_entry = tk.Entry(root, font=("Arial", 12), justify="center")
key_entry.pack(pady=5)

encrypt_btn = tk.Button(root, text="Encrypt Image", font=("Arial", 12), bg="#27ae60", fg="white", command=encrypt_image)
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(root, text="Decrypt Image", font=("Arial", 12), bg="#c0392b", fg="white", command=decrypt_image)
decrypt_btn.pack(pady=10)

root.mainloop()
