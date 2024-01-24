import sqlite3
import bcrypt

def create_user(username, password):
    conn = sqlite3.connect("game_progress.db")
    cursor = conn.cursor()

    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor.execute("INSERT INTO players (username, password_hash) VALUES (?, ?)",
                    (username, password_hash))
    conn.commit()
    print("User created successfully!")

    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect("game_progress.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM players WHERE username=?", (username,))
    result = cursor.fetchone()

    success = False

    if result is not None:
        password_hash = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), password_hash):
            print("Login successful!")
            success = True
        else:
            print("Incorrect password. Please try again.")
    else:
        print("User not found. Please check your username.")

    conn.close()
    return success

def get_unlocked_cats(username):
    return True

def get_cat(cat):
    return True

def get_achievments(username):
    return True