import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView


class AuthController:

    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        self.view.btn_login.configure(command=self.proses_login)

    def proses_login(self):
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get().strip()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan", "Username dan Password wajib diisi!"
            )
            return

        user = self.model.autentikasi(username, password)

        if user:
            messagebox.showinfo(
                "Login Berhasil",
                f"Selamat datang, {user['username']} ({user['role']})!",
            )

            # Sembunyikan window login
            self.view.withdraw()

            # Import di dalam fungsi untuk mencegah circular import
            from controllers.buku_controller import BukuController

            role_pengguna = user.get("role", "anggota")
            self.app_utama = BukuController(user_role=role_pengguna)

            # Hancurkan window login setelah app utama siap
            self.view.destroy()
            self.app_utama.run()
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")

    def run(self):
        self.view.mainloop()