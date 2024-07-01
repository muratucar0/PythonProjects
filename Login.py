import tkinter as tk
from tkinter import messagebox


def check_credentials():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Giriş Başarılı", "Hoş geldiniz, Admin!")
    else:
        messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya parola!")


root = tk.Tk()
root.title("Login Ekranı")


root.configure(bg="#3498db")


label_username = tk.Label(root, text="Kullanıcı Adı:", bg="#3498db", fg="white")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)


label_password = tk.Label(root, text="Parola:", bg="#3498db", fg="white")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)


button_login = tk.Button(root, text="Giriş Yap", command=check_credentials, bg="#2ecc71", fg="white")
button_login.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()