import tkinter as tk
from tkinter import ttk, messagebox
from database import get_connection, setup_login, check_login

BG = "#F3F5FB"
NAVY = "#192747"
BLUE = "#4361EE"
PURPLE = "#7657E8"
WHITE = "#FFFFFF"
TEXT = "#26334D"
MUTED = "#75819A"

TABLES = {
    "Mahasiswa": ("mahasiswa", "nim"),
    "Dosen": ("dosen", "nip"),
    "Mata Kuliah": ("mata_kuliah", "kode_mk"),
    "KRS": ("krs", "id_krs"),
    "Jadwal Kuliah": ("jadwal_kuliah", "id_jadwal"),
    "Pembayaran UKT": ("pembayaran_ukt", "id_pembayaran"),
}

class SiakadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SIAKAD | Teknik Informatika")
        self.root.geometry("1200x720")
        self.root.minsize(950, 600)
        self.root.configure(bg=BG)
        self.user = None
        self.current_label = None
        self.columns = []
        self.tree = None
        self.nav_buttons = {}
        self.setup_style()
        self.show_login()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=WHITE, foreground=TEXT,
                        rowheight=30, fieldbackground=WHITE,
                        font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#E3E9FF",
                        foreground=NAVY, font=("Segoe UI", 10, "bold"),
                        relief="flat")
        style.map("Treeview", background=[("selected", "#CCD7FF")],
                  foreground=[("selected", NAVY)])

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear()
        self.root.configure(bg="#EDF1FF")
        card = tk.Frame(self.root, bg=WHITE, highlightbackground="#DDE4F4",
                        highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center", width=430, height=490)
        tk.Frame(card, bg=BLUE, height=8).pack(fill="x")
        tk.Label(card, text="SIAKAD", bg=WHITE, fg=NAVY,
                 font=("Segoe UI", 29, "bold")).pack(pady=(30, 2))
        tk.Label(card, text="Sistem Informasi Akademik", bg=WHITE, fg=MUTED,
                 font=("Segoe UI", 11)).pack()
        tk.Label(card, text="TEKNIK INFORMATIKA", bg=WHITE, fg=PURPLE,
                 font=("Segoe UI", 9, "bold")).pack(pady=(5, 28))
        form = tk.Frame(card, bg=WHITE)
        form.pack(fill="x", padx=40)
        tk.Label(form, text="Username", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.username = ttk.Entry(form, font=("Segoe UI", 11))
        self.username.pack(fill="x", ipady=7, pady=(6, 15))
        tk.Label(form, text="Password", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.password = ttk.Entry(form, show="*", font=("Segoe UI", 11))
        self.password.pack(fill="x", ipady=7, pady=(6, 20))
        self.password.bind("<Return>", lambda event: self.login())
        tk.Button(form, text="MASUK KE SIAKAD", command=self.login,
                  bg=BLUE, fg=WHITE, activebackground="#3048C8",
                  activeforeground=WHITE, relief="flat", cursor="hand2",
                  font=("Segoe UI", 11, "bold"), pady=11).pack(fill="x")
        tk.Label(card, text="Login demo: admin | Password: admin123",
                 bg=WHITE, fg=MUTED, font=("Segoe UI", 9)).pack(pady=20)
        self.username.focus_set()

    def login(self):
        username = self.username.get().strip()
        password = self.password.get()
        if not username or not password:
            messagebox.showwarning("Login", "Username dan password harus diisi.")
            return
        try:
            user = check_login(username, password)
            if user:
                self.user = user
                self.show_dashboard()
            else:
                messagebox.showerror("Login gagal", "Username atau password salah.")
        except Exception as e:
            messagebox.showerror("Koneksi database",
                f"Tidak bisa mengakses MySQL.\n\n{e}\n\n"
                "Pastikan MySQL aktif dan database siakad sudah tersedia.")

    def show_dashboard(self):
        self.clear()
        self.root.configure(bg=BG)
        shell = tk.Frame(self.root, bg=BG)
        shell.pack(fill="both", expand=True)
        sidebar = tk.Frame(shell, bg=NAVY, width=225)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)
        tk.Label(sidebar, text="SIAKAD", bg=NAVY, fg=WHITE,
                 font=("Segoe UI", 25, "bold")).pack(anchor="w", padx=22, pady=(25, 0))
        tk.Label(sidebar, text="TEKNIK INFORMATIKA", bg=NAVY, fg="#B8C5FF",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=24, pady=(0, 28))
        tk.Label(sidebar, text="MENU UTAMA", bg=NAVY, fg="#9DAACC",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=22, pady=(0, 8))
        self.nav_buttons = {}
        self.add_nav(sidebar, "Dashboard", self.show_home)
        for label in TABLES:
            self.add_nav(sidebar, label, lambda item=label: self.show_table(item))
        tk.Button(sidebar, text="↪  Logout", command=self.logout,
                  bg=NAVY, fg="#FFCACA", activebackground="#304064",
                  activeforeground=WHITE, relief="flat", anchor="w",
                  padx=22, pady=12, font=("Segoe UI", 10),
                  cursor="hand2").pack(side="bottom", fill="x", pady=16)
        main = tk.Frame(shell, bg=BG)
        main.pack(side="left", fill="both", expand=True)
        topbar = tk.Frame(main, bg=WHITE, height=75)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)
        tk.Label(topbar, text="Sistem Informasi Akademik", bg=WHITE, fg=NAVY,
                 font=("Segoe UI", 16, "bold")).pack(side="left", padx=25)
        tk.Label(topbar, text=self.user["nama"], bg=WHITE, fg=PURPLE,
                 font=("Segoe UI", 10, "bold")).pack(side="right", padx=25)
        self.content = tk.Frame(main, bg=BG)
        self.content.pack(fill="both", expand=True, padx=25, pady=22)
        self.show_home()

    def add_nav(self, parent, label, command):
        btn = tk.Button(parent, text="▦   " + label, command=command,
                        bg=NAVY, fg=WHITE, activebackground="#354A9F",
                        activeforeground=WHITE, relief="flat", anchor="w",
                        padx=18, pady=11, font=("Segoe UI", 10), cursor="hand2")
        btn.pack(fill="x", padx=9, pady=2)
        self.nav_buttons[label] = btn

    def set_active(self, label):
        for name, btn in self.nav_buttons.items():
            btn.configure(bg="#354A9F" if name == label else NAVY)

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def run_query(self, sql, params=(), fetch=True):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(sql, params)
            result = cursor.fetchall() if fetch else None
            conn.commit()
            return result
        finally:
            cursor.close()
            conn.close()

    def get_columns(self, table):
        return self.run_query("""
            SELECT COLUMN_NAME, EXTRA, IS_NULLABLE, COLUMN_DEFAULT,
                   COLUMN_KEY, DATA_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
            ORDER BY ORDINAL_POSITION
        """, ("siakad", table))

    def show_home(self):
        self.clear_content()
        self.set_active("Dashboard")
        tk.Label(self.content, text="Dashboard", bg=BG, fg=NAVY,
                 font=("Segoe UI", 24, "bold")).pack(anchor="w")
        tk.Label(self.content, text="Ringkasan informasi akademik kampus.",
                 bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 20))
        cards = tk.Frame(self.content, bg=BG)
        cards.pack(fill="x")
        summary = [("Mahasiswa", "mahasiswa", BLUE), ("Dosen", "dosen", PURPLE),
                   ("Mata Kuliah", "mata_kuliah", "#079B83"),
                   ("Pembayaran UKT", "pembayaran_ukt", "#E49B25")]
        for i, (label, table, color) in enumerate(summary):
            card = tk.Frame(cards, bg=WHITE, highlightbackground="#E1E7F2", highlightthickness=1)
            card.grid(row=0, column=i, sticky="nsew", padx=(0 if i == 0 else 9, 0))
            cards.columnconfigure(i, weight=1, uniform="card")
            tk.Frame(card, bg=color, height=5).pack(fill="x")
            tk.Label(card, text=label, bg=WHITE, fg=MUTED,
                     font=("Segoe UI", 10)).pack(anchor="w", padx=15, pady=(15, 3))
            try:
                total = self.run_query(f"SELECT COUNT(*) AS total FROM `{table}`")[0]["total"]
            except Exception:
                total = "-"
            tk.Label(card, text=str(total), bg=WHITE, fg=NAVY,
                     font=("Segoe UI", 27, "bold")).pack(anchor="w", padx=15, pady=(0, 14))
        panel = tk.Frame(self.content, bg=WHITE, highlightbackground="#E1E7F2", highlightthickness=1)
        panel.pack(fill="both", expand=True, pady=(22, 0))
        tk.Label(panel, text="Selamat datang!", bg=WHITE, fg=NAVY,
                 font=("Segoe UI", 17, "bold")).pack(anchor="w", padx=22, pady=(25, 8))
        tk.Label(panel, text="Aplikasi SIAKAD Teknik Informatika membantu menampilkan dan mengelola data akademik kampus.",
                 bg=WHITE, fg=MUTED, font=("Segoe UI", 10), wraplength=650,
                 justify="left").pack(anchor="w", padx=22)
        tk.Label(panel, text="Gunakan menu di sebelah kiri untuk membuka data:",
                 bg=WHITE, fg=TEXT, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=22, pady=(22, 8))
        for label in TABLES:
            tk.Label(panel, text="✓   " + label, bg="#F0F3FF", fg="#344AA5",
                     font=("Segoe UI", 10, "bold"), padx=12, pady=7).pack(anchor="w", padx=22, pady=3)

    def show_table(self, label):
        messagebox.showinfo("Tahap 2", "Menu tabel akan dibuat pada Tahap 3.")

    def logout(self):
        if messagebox.askyesno("Logout", "Yakin ingin keluar dari SIAKAD?"):
            self.user = None
            self.show_login()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    try:
        setup_login()
        root.deiconify()
        app = SiakadApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Kesalahan aplikasi", f"Gagal menyiapkan database.\n\n{e}")
        root.destroy()
