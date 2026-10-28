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

    def make_button(self, parent, text, command, bg, fg):
        return tk.Button(parent, text=text, command=command, bg=bg, fg=fg,
                         activebackground=bg, activeforeground=fg, relief="flat",
                         padx=14, pady=8, font=("Segoe UI", 9, "bold"), cursor="hand2")

    def show_table(self, label):
        self.clear_content()
        self.current_label = label
        self.set_active(label)
        table, pk = TABLES[label]
        tk.Label(self.content, text=label, bg=BG, fg=NAVY,
                 font=("Segoe UI", 23, "bold")).pack(anchor="w")
        tk.Label(self.content, text=f"Data dari tabel {table}", bg=BG, fg=MUTED,
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 13))
        toolbar = tk.Frame(self.content, bg=BG)
        toolbar.pack(fill="x", pady=(0, 12))
        self.make_button(toolbar, "+ Tambah", self.add_record, BLUE, WHITE).pack(side="left", padx=(0, 7))
        self.make_button(toolbar, "Edit", self.edit_record, "#E2E8FF", NAVY).pack(side="left", padx=7)
        self.make_button(toolbar, "Hapus", self.delete_record, "#FFE3E3", "#B42318").pack(side="left", padx=7)
        self.make_button(toolbar, "Refresh", lambda: self.load_table(label), WHITE, TEXT).pack(side="right")
        frame = tk.Frame(self.content, bg=WHITE, highlightbackground="#E1E7F2", highlightthickness=1)
        frame.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(frame, show="headings", selectmode="browse")
        yscroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        xscroll = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(9, 0), pady=(9, 0))
        yscroll.grid(row=0, column=1, sticky="ns", pady=(9, 0))
        xscroll.grid(row=1, column=0, sticky="ew", padx=(9, 0), pady=(0, 9))
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        self.load_table(label)

    def load_table(self, label):
        table, pk = TABLES[label]
        try:
            rows = self.run_query(f"SELECT * FROM `{table}`")
            info = self.get_columns(table)
            self.columns = [item["COLUMN_NAME"] for item in info]
            self.tree.delete(*self.tree.get_children())
            self.tree["columns"] = self.columns
            for col in self.columns:
                self.tree.heading(col, text=col.replace("_", " ").title())
                self.tree.column(col, width=max(110, min(190, len(col) * 11)), minwidth=90, anchor="w")
            for row in rows:
                values = ["" if row.get(col) is None else str(row.get(col)) for col in self.columns]
                self.tree.insert("", "end", values=values)
        except Exception as e:
            messagebox.showerror("Gagal memuat data", str(e))

    def selected_row(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Pilih data", "Pilih satu baris pada tabel terlebih dahulu.")
            return None
        return dict(zip(self.columns, self.tree.item(selected[0], "values")))

    def record_form(self, title, fields, initial=None, readonly=None):
        initial = initial or {}
        readonly = set(readonly or [])
        result = {}
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("540x620")
        win.minsize(440, 350)
        win.configure(bg=WHITE)
        win.transient(self.root)
        win.grab_set()
        tk.Label(win, text=title, bg=WHITE, fg=NAVY,
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=20, pady=(18, 10))
        canvas = tk.Canvas(win, bg=WHITE, highlightthickness=0)
        scrollbar = ttk.Scrollbar(win, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg=WHITE)
        window_id = canvas.create_window((0, 0), window=inner, anchor="nw")
        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfigure(window_id, width=e.width))
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True, padx=(18, 0))
        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=8)
        widgets = {}
        for field in fields:
            col = field["COLUMN_NAME"]
            if "auto_increment" in (field["EXTRA"] or "").lower():
                continue
            tk.Label(inner, text=col.replace("_", " ").title(), bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=4, pady=(7, 2))
            entry = ttk.Entry(inner, font=("Segoe UI", 10))
            entry.pack(fill="x", padx=4, ipady=5, pady=(0, 5))
            value = initial.get(col, "")
            if value is not None:
                entry.insert(0, str(value))
            if col in readonly:
                entry.configure(state="readonly")
            widgets[col] = entry
        def save():
            for col, entry in widgets.items():
                result[col] = entry.get().strip()
            win.destroy()
        tk.Button(win, text="Simpan", command=save, bg=BLUE, fg=WHITE,
                  activebackground="#3048C8", activeforeground=WHITE,
                  relief="flat", padx=20, pady=9,
                  font=("Segoe UI", 10, "bold")).pack(pady=12)
        self.root.wait_window(win)
        return result if result else None

    def add_record(self):
        label = self.current_label
        table, pk = TABLES[label]
        try:
            fields = self.get_columns(table)
            values = self.record_form("Tambah " + label, fields)
            if values is None:
                return
            data = {}
            for field in fields:
                col = field["COLUMN_NAME"]
                if col not in values:
                    continue
                value = values[col]
                if value == "" and (field["IS_NULLABLE"] == "YES" or field["COLUMN_DEFAULT"] is not None):
                    data[col] = None
                else:
                    data[col] = value
            if not data:
                return
            cols = list(data.keys())
            sql = (f"INSERT INTO `{table}` ({', '.join('`' + c + '`' for c in cols)}) "
                   f"VALUES ({', '.join(['%s'] * len(cols))})")
            self.run_query(sql, tuple(data[c] for c in cols), fetch=False)
            self.load_table(label)
            messagebox.showinfo("Berhasil", "Data berhasil ditambahkan.")
        except Exception as e:
            messagebox.showerror("Gagal menambah data", f"Periksa input dan hubungan foreign key.\n\n{e}")

    def edit_record(self):
        row = self.selected_row()
        if row is None:
            return
        label = self.current_label
        table, pk = TABLES[label]
        try:
            fields = self.get_columns(table)
            values = self.record_form("Edit " + label, fields, initial=row, readonly=[pk])
            if values is None:
                return
            update_cols = [f["COLUMN_NAME"] for f in fields
                           if f["COLUMN_NAME"] != pk and f["COLUMN_NAME"] in values]
            if not update_cols:
                return
            assignments = ", ".join(f"`{col}`=%s" for col in update_cols)
            params = [values[col] if values[col] != "" else None for col in update_cols]
            params.append(row[pk])
            self.run_query(f"UPDATE `{table}` SET {assignments} WHERE `{pk}`=%s",
                           tuple(params), fetch=False)
            self.load_table(label)
            messagebox.showinfo("Berhasil", "Data berhasil diperbarui.")
        except Exception as e:
            messagebox.showerror("Gagal mengedit data", f"Periksa input dan hubungan foreign key.\n\n{e}")

    def delete_record(self):
        row = self.selected_row()
        if row is None:
            return
        label = self.current_label
        table, pk = TABLES[label]
        if not messagebox.askyesno("Konfirmasi hapus",
                f"Hapus data dengan {pk} = {row[pk]}?\n\n"
                "Data yang masih digunakan tabel lain mungkin tidak dapat dihapus."):
            return
        try:
            self.run_query(f"DELETE FROM `{table}` WHERE `{pk}`=%s", (row[pk],), fetch=False)
            self.load_table(label)
            messagebox.showinfo("Berhasil", "Data berhasil dihapus.")
        except Exception as e:
            messagebox.showerror("Gagal menghapus data", f"Data mungkin masih digunakan oleh tabel lain.\n\n{e}")

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
        messagebox.showerror("Kesalahan aplikasi",
            "Tidak dapat terhubung atau menyiapkan database.\n\n"
            f"{e}\n\nPastikan MySQL XAMPP aktif, database siakad tersedia, "
            "dan pengaturan di database.py sudah benar.")
        root.destroy()
