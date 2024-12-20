class Contact:
    def __init__(self, id, name, phone, email, address):
        self._id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    @property
    def id(self):
        return self._id


RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


def print_colored(text, color=RED):
    # Bu funksiya quiydagi link orqali yozildi : https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
    print(f"{color}{text}{RESET}", end="")


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


def getContactById(id):
    for contact in contactList:
        if contact.id == id:
            return contact
    return -1


def showContacts(contactList: list):
    if len(contactList) != 0:
        for contact in contactList:
            print("= " * 5 + f' ID:{contact.id}  ' + "= " * 5)
            print(f"{lang['name']} {contact.name}")
            print(f"{lang['phone']} {contact.phone}")
            print(f"{lang['email']} {contact.email}")
            print(f"{lang['address']} {contact.address}")
            print("= " * 13)
    else:
        print_colored(f"{lang['list_empty']}\n")


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
    "invalid_choice": "Xato tanlangan bo`lim",
    "success_edit": "Contact muvaffaqiyatli o`zgartirildi.",
    "error_edit": "Contact o`zgartirishda  Email yoki Telefon raqami xato formatda.",
    "success_delete": "Contact muvaffaqiyatli o`chirildi.",
    "success_add": "Contact qo`shildi.",
    "phone": "Telefon: ",
    "name": "Ism: ",
    "email": "Email: ",
    "address": "Yashash manzil: ",
    "list_empty": "Contact ro`yxati bo`sh",
    "current_phone": "Hozirgi telefon raqami: ",
    "current_email": "Hozirgi email: ",
    "current_address": "Hozirgi yashash manzil: ",
    "new_phone": "Yangi telefon raqami: ",
    "new_email": "Yangi email: ",
    "new_address": "Yangi yashash manzil: ",
    "current_name": "Hozirgi ism: ",
    "new_name": "Yangi ism: ",
    "uz_lang":"1.O'zbekcha",
    "eng_lang":"2.English",
    "invalid_id": "Xato id",
    "choose_lang": "Tilni tanlang: ",
    "exit": "Chiqildi !",
}
eng = {
    "1": "1.Add contact",
    "2": "2.Edit contact",
    "3": "3.Delete contact",
    "4": "4.Search contact",
    "5": "5.Contact list",
    "6": "6.Change language",
    "7": "7.Exit",
    "uz_lang": "1.Uzbek",
    "eng_lang": "2.English",
    "choose_lang": "Choose language: ",
    "choice": "Choose section: ",
    "input_name": "Enter name: ",
    "input_phone": "Enter phone number (+998XXXXXXXXX): ",
    "input_email": "Enter email (someone@gmail.com): ",
    "input_address": "Enter address: ",
    "invalid_phone": "Invalid phone number, enter in the correct format",
    "invalid_email": "Invalid email, enter in the correct format",
    "invalid_choice": "Invalid choice",
    "success_add": "Contact added.",
    "exit": "Exited !",
    "phone": "Phone: ",
    "name": "Name: ",
    "email": "Email: ",
    "address": "Address: ",
    "list_empty": "Contact list is empty",
    "invalid_id": "Invalid id",
    "current_phone": "Current phone number: ",
    "current_email": "Current email: ",
    "success_edit": "Contact edited.",
    "current_address": "Current address: ",
    "new_phone": "New phone number: ",
    "new_email": "New email: ",
    "success_delete": "Contact deleted.",
    "error_edit": "Email or phone number is in the wrong format.",
    "new_address": "New address: ",
    "current_name": "Current name: ",
    "new_name": "New name: ",
}

lang = uz


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
            while True:
                phone = input(lang["input_phone"])
                if not checkPhone(phone):
                    print_colored(f"{lang['invalid_phone']}\n")
                else:
                    break
            while True:
                email = input(lang["input_email"])
                if not checkEmail(email):
                    print_colored(f"{lang['invalid_email']}\n")
                else:
                    break
            address = input(lang["input_address"])
            contact = Contact(len(contactList) + 1, name, phone, email, address)
            contactList.append(contact)
            print_colored(f"{lang['success_add']}\n", GREEN)
        elif choice == "2":
            showContacts(contactList)
            id = int(input("ID: "))
            contactData = getContactById(id)
            if contactData == -1:
                print_colored(f"{lang['invalid_id']}\n", RED)
            else:
                print("= " * 5 + f' ID:{contactData.id}  ' + "= " * 5)
                new_name = input(f"{lang['input_name']} ({lang['current_name']}: {contactData.name}):")
                new_phone = input(f"{lang['input_phone']} ({lang['current_phone']}: {contactData.phone})")
                new_email = input(f"{lang['input_email']} ({lang['current_email']}: {contactData.email})")
                new_address = input(f"{lang['input_address']} ({lang['current_address']}: {contactData.address})")

                if checkEmail(contactData.email) and checkPhone(contactData.phone):
                    contactData.name = contactData.name if new_name == "" else new_name
                    contactData.phone = contactData.phone if new_phone == "" else new_phone
                    contactData.email = contactData.email if new_email == "" else new_email
                    contactData.address = contactData.address if new_address == "" else new_address
                    print_colored(f"{lang['success_edit']}\n", GREEN)
                else:
                    print_colored(f"{lang['error_edit']}\n", RED)
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print(f"{lang['uz_lang']}")
            print(f"{lang['eng_lang']}")
            newLang = input(f"{lang['choose_lang']}")
            if newLang == "1":
                lang = uz
            elif newLang == "2":
                lang = eng
            else:
                print_colored(f"{lang['invalid_choice']}\n", RED)
        elif choice == "7":
            break
        else:
            print_colored(f"{lang['invalid_choice']}\n", RED)


main_page()
