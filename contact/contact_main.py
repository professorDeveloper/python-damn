class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self._phone = phone
        self._email = email
        self.address = address

    @property
    def phone(self):
        return self._phone

    @phone.setter
    #  check phone number  +998943017410
    def phone(self, phone):
        if phone.startswith("+998") and len(phone) == 13:
            self._phone = phone
        else:
            print("Telefon raqam xato format xato, ko`rsatilgan xolatda kiriting")


contactList = []
uz = {
    "1": "1.Contact qo`shish",
    "2": "2.Contact o`zgartirish",
    "3": "3.Contact o`chirish",
    "4": "4.Contactni qidirish",
    "5": "5.Contactni ro`yxatini ko`rish",
    "6": "6.Tilni o`zgartirish",
    "7": "7.Chiqish",
    "choice": "Bo`limni tanlang: ",
    "input_name": "Ismni kiriting: ",
    "input_phone": "Telefon raqamni kiriting (+998XXXXXXXXX): ",
    "input_email": "email pochta (someone@gmail.com): ",
    "input_address": "Yashash manzil: ",
    "invalid_phone": "Telefon raqam xato format xato, ko`rsatilgan xolatda kiriting",
    "invalid_email": "Email xato format xato, ko`rsatilgan xolatda kiriting",
    "success_add": "Contact qo`shildi.",
}
eng = {
    "1": "1.Add contact",
    "2": "2.Edit contact",
    "3": "3.Delete contact",
    "4": "4.Search contact",
    "5": "5.Contact list",
    "6": "6.Change language",
    "7": "7.Exit",
    "choice": "Choose section: ",
    "input_name": "Enter name: ",
    "input_phone": "Enter phone number (+998XXXXXXXXX): ",
    "input_email": "Enter email (someone@gmail.com): ",
    "input_address": "Enter address: ",
    "invalid_phone": "Invalid phone number, enter in the correct format",
    "invalid_email": "Invalid email, enter in the correct format",
    "success_add": "Contact added.",
}

lang = uz


def checkPhone(phone):
    if phone.startswith("+998") and len(phone) == 13:
        return True
    else:
        return False


def checkEmail(email: str):
    if email.endswith("@gmail.com") or email.endswith("@yahoo.com") or email.endswith("@hotmail.com"):
        return True
    else:
        return False


def main_page():
    print("Contact App.")
    while True:
        print(f"{lang['1']}")
        print(f"{lang['2']}")
        print(f"{lang['3']}")
        print(f"{lang['4']}")
        print(f"{lang['5']}")
        print(f"{lang['6']}")
        print(f"{lang['7']}")
        choice = input(lang["choice"])
        if choice == "1":
            name = input(lang["input_name"])
            phone = input(lang["input_phone"])
            email = input(lang["input_email"])
            address = input(lang["input_address"])
            if not checkPhone(phone):
                print(lang["invalid_phone"])
            elif not checkEmail(email):
                print(lang["invalid_email"])
            else:
                contact = Contact(name, phone, email, address)
                contactList.append(contact)
                print(lang["success_add"])

        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            break


main_page()