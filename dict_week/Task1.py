my_dict = {}

while True:
    print()
    print("1-> Add Dictionary")
    print("2-> Search Dictionary by Eng")
    print("3-> Delete Dictionary by Eng")
    print("4-> Display Dictionary List")
    print("5-> Edit Dictionary by Eng")
    print("6-> Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("English word: ")
        uz_word = input("Uz word: ")
        my_dict[word.lower()] = uz_word.lower()
        print("Dictionary added")

    elif choice == "2":
        query = input("Search english word: ")
        print("========= Search result =========")
        if query.lower() in my_dict:
            print(query.lower(), f"- {my_dict[query].lower()}")
        else:
            print("Word not found")
        print("=================================")

    elif choice == "3":
        query = input("Enter english word to delete: ")
        print(my_dict.pop(query.lower(), "Word not found"))

    elif choice == "4":
        print("========= Dictionary List =========")
        for word in my_dict:
            print(word, f"- {my_dict[word]}")
        print("===================================")
    elif choice == "5":
        edit = input("Enter edit english word ")
        updateData =my_dict[edit]
        my_dict.pop(edit,"Word not found")
        newWord = input("New uz word: ")
        my_dict.update({edit: newWord})
    elif choice == "6":
        print("========= Exiting ==========")
        break

    else:
        print("Invalid choice")
