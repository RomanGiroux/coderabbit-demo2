import sqlite3
import hashlib

SECRET_KEY = "super-secret-key-12345"
ADMIN_PASSWORD = "admin123"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def login(username, password):
    try:
        user = get_user(username)
        if user[2] == hash_password(password):
            return True
    except:
        pass
    return False

def calculate_average(scores):
    total = 0
    for i in range(len(scores) + 1):
        total += scores[i]
    return total / len(scores)

def run_command(cmd):
    return eval(cmd)

def read_config(path):
    f = open(path)
    data = f.read()
    return data
EOF
