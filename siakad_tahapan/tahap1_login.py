import tkinter as tk
from tkinter import ttk, messagebox
from database import setup_login, check_login

def login():
    username = entry_username.get().strip()
    password = entry_password.get()
    if not username or not password:
        messagebox.showwarning("Login", "Username dan password harus diisi.")
        return
    try:
        user = check_login(username, password)
        if user:
            messagebox.showinfo("Berhasil", f"Selamat datang, {user['nama']}!")
        else:
            messagebox.showerror("Login gagal", "Username atau password salah.")
    except Exception as e:
        messagebox.showerror("Koneksi database", f"Tidak bisa mengakses MySQL.\n\n{e}")

root = tk.Tk()
root.title("SIAKAD | Tahap 1 - Login")
root.geometry("430x390")
root.configure(bg="#F3F5FB")
try:
    setup_login()
except Exception as e:
    messagebox.showerror("Database", f"Gagal menyiapkan database.\n\n{e}")
    root.destroy()
    raise SystemExit

tk.Label(root, text="SIAKAD", bg="#F3F5FB", fg="#192747",
         font=("Segoe UI", 28, "bold")).pack(pady=(30, 4))
tk.Label(root, text="Sistem Informasi Akademik", bg="#F3F5FB",
         fg="#75819A", font=("Segoe UI", 11)).pack(pady=(0, 22))
tk.Label(root, text="Username", bg="#F3F5FB").pack()
entry_username = ttk.Entry(root, width=34)
entry_username.pack(pady=5, ipady=4)
tk.Label(root, text="Password", bg="#F3F5FB").pack()
entry_password = ttk.Entry(root, width=34, show="*")
entry_password.pack(pady=5, ipady=4)
entry_password.bind("<Return>", lambda event: login())
tk.Button(root, text="MASUK", command=login, bg="#4361EE", fg="white",
          relief="flat", padx=30, pady=9).pack(pady=18)
tk.Label(root, text="Demo: admin / admin123", bg="#F3F5FB",
         fg="#75819A").pack()
entry_username.focus_set()
root.mainloop()
