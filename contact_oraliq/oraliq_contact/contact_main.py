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

contactList = []
uz = {
    "1": "1.Contact qo`shish",
    "2": "2.Contact o`zgartirish",
    "3": "3.Contact o`chirish",
    "4": "4.Contactni qidirish",
    "5": "5.Contactni ro`yxatini ko`rish",
    "6": "6.Tilni o`zgartirish",
    "7": "7.Chiqish",
    "not_found": "Contact Topilmadi !",
    "contact_deleted": "Contact o`chirildi !",
    "input_email": "Emailni kiriting: ",
    "input_address": "Yashash manzilni kiriting: ",
    "search_input": "Qidirmoqchi bo`lgan Contact nomi yoki telefon raqamini kiriting:",
    "choice": "Bo`limni tanlang: ",
    "input_name": "Ismni kiriting: ",
    "input_address": "Yashash manzil: ",
    "invalid_choice": "Xato tanlangan bo`lim",
    "want_exit": "Rostdan ham dasturdan chiqmoqchimisiz y/n ?",
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
    "input_phone": "Telefon raqamini kiriting: ",
    "new_email": "Yangi email: ",
    "new_address": "Yangi yashash manzil: ",
    "contact_empty": "ContactList bo`sh !",
    "current_name": "Hozirgi ism: ",
    "new_name": "Yangi ism: ",
    "uz_lang": "1.O'zbekcha",
    "eng_lang": "2.English",
    "invalid_id": "Xato id",
    "cancelled": "Vazifa bekor qilindi",
    "choose_lang": "Tilni tanlang: ",
    "sure_delete": "Rostdan ham bu contactni o`chirmoqchimisiz ? y/n",
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
    "contact_empty": "ContactList empty !",
    "not_found": "Contact not found !",
    "want_exit": "Are you sure you want to log out y/n ?",
    "contact_deleted": "Contact Deleted !",
    "choice": "Choose section: ",
    "input_name": "Enter name: ",
    "cancelled": "Task Cancelled",
    "search_input": "Enter the name or phone number of the Contact you want to search for:",
    "input_phone": "Enter phone number: ",
    "input_email": "Enter email : ",
    "input_address": "Enter address: ",
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
    "sure_delete": "Do you really want to delete this contact? y/n",

    "current_email": "Current email: ",
    "success_edit": "Contact edited.",
    "current_address": "Current address: ",

    "new_phone": "New phone number: ",
    "new_email": "New email: ",
    "success_delete": "Contact deleted.",
    "new_address": "New address: ",
    "current_name": "Current name: ",
    "new_name": "New name: ",
}

lang = uz


def print_colored(text, color=RED):
    # Bu funksiya quiydagi link orqali yozildi : https://stackoverflow.com/questions/287871/how-to-print-colored-text
    # -in-python
    print(f"{color}{text}{RESET}", end="")


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


def showContact(contact: Contact):
    print("= " * 5 + f' ID:{contact.id}  ' + "= " * 5)
    print(f"{lang['name']} {contact.name}")
    print(f"{lang['phone']} {contact.phone}")
    print(f"{lang['email']} {contact.email}")
    print(f"{lang['address']} {contact.address}")
    print("= " * 13)


def deleteContactById(id: int):
    contact = getContactById(id)
    if contact != -1:
        choice = input(lang['sure_delete']+": ")
        if choice == 'y':
            contactList.remove(contact)
            print_colored(lang['contact_deleted']+"\n", GREEN)
        else:
            print_colored(lang['cancelled']+"\n", RED)
    else:
        print(lang['invalid_id'])


def editContactById(id: int):
    contactData = getContactById(id)
    if contactData == -1:
        print_colored(f"{lang['invalid_id']}\n", RED)
    else:
        print("= " * 5 + f' ID:{contactData.id}  ' + "= " * 5)
        new_name = input(f"{lang['input_name']} ({lang['current_name']}: {contactData.name}):")
        new_phone = input(f"({lang['current_phone']}: {contactData.phone}):")
        new_email = input(f"{lang['input_email']} ({lang['current_email']}: {contactData.email})")
        new_address = input(f"{lang['input_address']} ({lang['current_address']}: {contactData.address})")
        contactData.name = contactData.name if new_name == "" else new_name
        contactData.phone = contactData.phone if new_phone == "" else new_phone
        contactData.email = contactData.email if new_email == "" else new_email
        contactData.address = contactData.address if new_address == "" else new_address
        print_colored(f"{lang['success_edit']}\n", GREEN)


def addContact():
    name = input(lang["input_name"])
    phone = input(lang["input_phone"])
    email = input(lang["input_email"])
    address = input(lang["input_address"])
    contact = Contact(len(contactList) + 1, name, phone, email, address)
    contactList.append(contact)
    print_colored(f"{lang['success_add']}\n", GREEN)


def searchContact(query: str):
    results =[]
    contact = None
    if len(contactList) != -1:
        for contact in contactList:
            if query.lower() in contact.name.lower() or query.lower() in contact.phone.lower():
                results.append(contact)
        if len(results) !=0:
            showContacts(results)
        else:
            print_colored(lang['not_found'], RED)
        del results
    else:
        print_colored(lang['contact_empty'], RED)


def changeLanguage():
    global lang
    print(f"{lang['uz_lang']}")
    print(f"{lang['eng_lang']}")
    newLang = input(f"{lang['choose_lang']}")
    if newLang == "1":
        lang = uz
    elif newLang == "2":
        lang = eng
    else:
        print_colored(f"{lang['invalid_choice']}\n", RED)


def exitProgram():
    wantExit = False
    choice = input(lang['want_exit']+":")
    if choice == 'y':
        wantExit = True
    else:
        print_colored(lang['cancelled'], RED)
    return wantExit


def main_page():
    global lang
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
            addContact()
        elif choice == "2":
            showContacts(contactList)
            id = input("ID: ")
            if not id.isdigit():
                print_colored(f"{lang['invalid_id']}\n", RED)
            else:
                editContactById(int(id))

        elif choice == "3":
            showContacts(contactList)
            id = input("ID: ")
            if not id.isdigit():
                print_colored(f"{lang['invalid_id']}\n", RED)
            else:
                deleteContactById(int(id))

        elif choice == "4":
            query = input(lang['search_input'])
            searchContact(query)
        elif choice == "5":
            showContacts(contactList)
        elif choice == "6":
            changeLanguage()
        elif choice == "7":
            if exitProgram():
                break
        else:
            print_colored(f"{lang['invalid_choice']}\n", RED)


main_page()
