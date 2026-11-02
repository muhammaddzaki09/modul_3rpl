import customtkinter as ctk
from tkinter import ttk

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Aplikasi Perpustakaan - Manajemen Anggota")
        self.geometry("950x500")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Frame Form Kiri
        self.frame_form = ctk.CTkFrame(self, width=320)
        self.frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.label_title = ctk.CTkLabel(self.frame_form, text="Form Data Anggota", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=20)
        
        self.entry_nama = ctk.CTkEntry(self.frame_form, placeholder_text="Masukkan Nama Lengkap")
        self.entry_nama.pack(pady=10, padx=20, fill="x")
        
        self.entry_alamat = ctk.CTkEntry(self.frame_form, placeholder_text="Masukkan Alamat")
        self.entry_alamat.pack(pady=10, padx=20, fill="x")
        
        self.btn_simpan = ctk.CTkButton(self.frame_form, text="Simpan Anggota", fg_color="green", hover_color="darkgreen")
        self.btn_simpan.pack(pady=10, padx=20, fill="x")
        
        self.btn_perbarui = ctk.CTkButton(self.frame_form, text="Perbarui Anggota", fg_color="blue", hover_color="darkblue")
        self.btn_perbarui.pack(pady=10, padx=20, fill="x")
        
        self.btn_hapus = ctk.CTkButton(self.frame_form, text="Hapus Anggota", fg_color="red", hover_color="darkred")
        self.btn_hapus.pack(pady=10, padx=20, fill="x")
        
        # Frame Tabel Kanan
        self.frame_tabel = ctk.CTkFrame(self)
        self.frame_tabel.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.label_tabel = ctk.CTkLabel(
            self.frame_tabel, 
            text="Daftar Anggota Perpustakaan Muhammad Dzaki Kurniawan_F5212530102", 
            font=("Arial", 14, "bold")
        )
        self.label_tabel.pack(pady=15)
        
        self.tabel = ttk.Treeview(self.frame_tabel, columns=("id", "nama", "alamat"), show="headings")
        self.tabel.heading("id", text="ID")
        self.tabel.heading("nama", text="Nama Lengkap")
        self.tabel.heading("alamat", text="Alamat")
        
        self.tabel.column("id", width=50, anchor="center")
        self.tabel.column("nama", width=180, anchor="w")
        self.tabel.column("alamat", width=250, anchor="w")
        
        self.tabel.pack(pady=10, padx=10, fill="both", expand=True)