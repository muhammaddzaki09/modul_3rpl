import hashlib
from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    @staticmethod
    def hash_password(password):
        """Mengubah password plaintext menjadi string hash SHA-256."""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        """Memeriksa keberadaan pengguna dan kesesuaian password ter-hash."""
        if not self.conn:
            return None
        
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        hashed_pw = self.hash_password(password)
        cursor.execute(query, (username, hashed_pw))
        user = cursor.fetchone()
        cursor.close()
        return user