import hashlib
from config.database import Database

class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if not self.conn:
            return None

        cursor = self.conn.cursor(dictionary=True)
        # Meng-hash input password sebelum dicocokkan ke database
        hashed_pw = self.hash_password(password)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, hashed_pw))
        
        user = cursor.fetchone()
        cursor.close()
        return user