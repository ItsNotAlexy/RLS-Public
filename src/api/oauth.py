import requests
import json
import sqlite3

class Oauth():
    def __init__(self, player, id):
        self.player = player
        self.id = id
        
    def is_whitelisted(self):
        conn = sqlite3.connect('./src/api/database/auth.db')
        c = conn.cursor()
        c.execute("SELECT * FROM whitelist WHERE id = ?", (self.id,))
        if c.fetchone() is None:
            return False
        else:
            return True
        
    def add_whitelisted(self):
        conn = sqlite3.connect('./src/api/database/auth.db')
        c = conn.cursor()
        c.execute("INSERT INTO whitelist VALUES (? )", (self.id,))
        conn.commit()
        conn.close()

    def remove_whitelisted(self):
        conn = sqlite3.connect('./src/api/database/auth.db')
        c = conn.cursor()
        c.execute("DELETE FROM whitelist WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
