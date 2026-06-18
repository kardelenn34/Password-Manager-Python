import sqlite3

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

conn.commit()


def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    cursor.execute("""
    INSERT INTO passwords(website, username, password)
    VALUES (?, ?, ?)
    """, (website, username, password))

    conn.commit()
    print("\nPassword added successfully.\n")


def view_passwords():
    cursor.execute("SELECT * FROM passwords")

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("\nNo passwords found.\n")
        return

    print("\n===== SAVED PASSWORDS =====\n")

    for row in rows:
        print(f"ID: {row[0]}")
        print(f"Website: {row[1]}")
        print(f"Username: {row[2]}")
        print(f"Password: {row[3]}")
        print("-" * 30)


def delete_password():
    password_id = input("Enter ID to delete: ")

    cursor.execute(
        "DELETE FROM passwords WHERE id = ?",
        (password_id,)
    )

    conn.commit()
    print("\nPassword deleted.\n")


def search_password():
    website = input("Website name: ")

    cursor.execute(
        "SELECT * FROM passwords WHERE website LIKE ?",
        (f"%{website}%",)
    )

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("\nNo matching records found.\n")
        return

    for row in rows:
        print(f"\nID: {row[0]}")
        print(f"Website: {row[1]}")
        print(f"Username: {row[2]}")
        print(f"Password: {row[3]}")
        print("-" * 30)


def close_connection():
    conn.close()