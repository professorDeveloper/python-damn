from programming_assigment.util.util import println_colored, Color
from data.local_data import eng, uz
from data.main_func import signIn, signUp

language = uz


def setUpMain():
    global language
    while True:
        println_colored(f"1.{language['signin']}", Color.GREEN)
        println_colored(f"2.{language['signUp']}", Color.CYAN)
        println_colored(f"3.{language['lang']}", Color.MAGENTA)
        println_colored("==================================", Color.DARK_ORANGE)

        choose = input(language['choice'])
        if choose == '1':
            login = input(language['input_login'] + ":")
            password = input(language['input_password'] + ":")
            signIn(login, password, language)

        elif choose == '2':
            name = input(f"{language['name']}:")
            login = input(f"{language['input_login']}:")
            password = input(f"{language['input_password']}:")
            signUp(name, password, login,language)

        elif choose == '3':
            println_colored("==================================", Color.BLUE)
            print("1.uz 2.eng")
            lang_choice = input(language['choice'])

            if lang_choice == '1':
                language = uz  # Tilni o'zgartiramiz
            elif lang_choice == '2':
                language = eng
            else:
                println_colored(language['invalid_choice'], Color.RED)

        else:
            println_colored(language['invalid_choice'], Color.RED)

setUpMain()