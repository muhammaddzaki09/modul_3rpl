from models.buku_model import BukuModel

# Jangan biarkan pemanggilan fungsi berjalan langsung di level paling atas file (top-level)
if __name__ == "__main__":
    model = BukuModel()
    buku_list = model.get_all_buku()
    if buku_list:
        id_terakhir = buku_list[-1]["id_buku"]
        print(f"ID Buku Terakhir: {id_terakhir}")
    else:
        print("Daftar buku kosong.")