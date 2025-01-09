import sqlite3
from datetime import datetime


# Ma'lumotlar bazasini yaratish va ulanish
def init_db():
    conn = sqlite3.connect("car_numbers.db")
    cursor = conn.cursor()

    # Raqamlar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL UNIQUE,
            price REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)

    # Foydalanuvchilar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            purchased_numbers TEXT
        )
    """)

    # Sotuvlar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES Users(id)
        )
    """)

    conn.commit()
    conn.close()


# Raqam qo'shish
def add_number(number, price):
    conn = sqlite3.connect("car_numbers.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Numbers (number, price, status) VALUES (?, ?, ?)", (number, price, "available"))
    conn.commit()
    conn.close()
    print(f"Raqam {number} muvaffaqiyatli qo'shildi.")


# Raqamlar ro'yxatini ko'rish
def view_available_numbers():
    conn = sqlite3.connect("car_numbers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Numbers WHERE status = 'available'")
    numbers = cursor.fetchall()
    conn.close()
    print("Mavjud raqamlar:")
    for number in numbers:
        print(f"ID: {number[0]}, Raqam: {number[1]}, Narx: {number[2]}")


# Raqamni sotish
def sell_number(number, user_name, user_address):
    conn = sqlite3.connect("car_numbers.db")
    cursor = conn.cursor()

    # Tekshirish: raqam mavjudmi va sotuvda bo'lganmi?
    cursor.execute("SELECT * FROM Numbers WHERE number = ? AND status = 'available'", (number,))
    number_data = cursor.fetchone()
    if not number_data:
        print("Raqam mavjud emas yoki allaqachon sotilgan.")
        return

    # Foydalanuvchini qo'shish yoki yangilash
    cursor.execute("SELECT * FROM Users WHERE name = ?", (user_name,))
    user_data = cursor.fetchone()

    if not user_data:
        cursor.execute("INSERT INTO Users (name, address, purchased_numbers) VALUES (?, ?, ?)",
                       (user_name, user_address, number))
        user_id = cursor.lastrowid
    else:
        user_id = user_data[0]
        purchased_numbers = user_data[3] + f", {number}" if user_data[3] else number
        cursor.execute("UPDATE Users SET purchased_numbers = ? WHERE id = ?", (purchased_numbers, user_id))

    # Raqamni sotilgan deb belgilash
    cursor.execute("UPDATE Numbers SET status = 'sold' WHERE number = ?", (number,))

    # Sotuvni qo'shish
    cursor.execute("INSERT INTO Sales (number, user_id, date) VALUES (?, ?, ?)",
                   (number, user_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()
    print(f"Raqam {number} foydalanuvchi {user_name}ga sotildi.")


# Xarid tarixini ko'rish
def view_purchase_history(user_name):
    conn = sqlite3.connect("car_numbers.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE name = ?", (user_name,))
    user_data = cursor.fetchone()

    if not user_data:
        print("Foydalanuvchi topilmadi.")
        return

    print(f"{user_name} xarid qilgan raqamlar: {user_data[3]}")


# Asosiy menyu
def main():
    init_db()
    while True:
        print("\nAvtomobil raqamlarini sotish dasturi")
        print("1. Raqam qo'shish")
        print("2. Mavjud raqamlarni ko'rish")
        print("3. Raqamni sotish")
        print("4. Xarid tarixini ko'rish")
        print("5. Chiqish")

        choice = input("Tanlovingizni kiriting: ")
        if choice == "1":
            number = input("Raqamni kiriting: ")
            price = float(input("Narxni kiriting: "))
            add_number(number, price)
        elif choice == "2":
            view_available_numbers()
        elif choice == "3":
            number = input("Sotiladigan raqamni kiriting: ")
            user_name = input("Foydalanuvchi ismini kiriting: ")
            user_address = input("Foydalanuvchi manzilini kiriting: ")
            sell_number(number, user_name, user_address)
        elif choice == "4":
            user_name = input("Foydalanuvchi ismini kiriting: ")
            view_purchase_history(user_name)
        elif choice == "5":
            print("Dasturdan chiqildi.")
        else:
            print("Noto'g'ri tanlov.")
main()